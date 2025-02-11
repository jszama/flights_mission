import vertexai
import streamlit as st
from vertexai.preview.generative_models import GenerationConfig, GenerativeModel, Tool, ToolConfig, Part, Content, ChatSession
from services.flight_manager import search_flights, book_flight, update_flight_booking, remove_flight_booking, find_booking_id, find_customer_id, find_flight_id

from functions.flight import (
    find_booking_id_func,
    find_customer_id_func,
    find_flight_id_func,
    get_search_flights_func,
    handle_booking_flights_func,
    handle_removing_booking_func,
    handle_update_booking_func,
)

class Agent:
    def __init__(self):
        self.chat = None
        self.messages = []

        project = "trans-array-427509-h2"
        vertexai.init(project=project)

        self.tools = Tool(
            function_declarations=[handle_booking_flights_func, get_search_flights_func, handle_removing_booking_func, handle_update_booking_func, find_booking_id_func,find_customer_id_func,find_flight_id_func]
        )

        # tool config used for forced function calling. However, its only used for testing purposes
        self.tool_config = ToolConfig(
            function_calling_config=ToolConfig.FunctionCallingConfig(
                mode=ToolConfig.FunctionCallingConfig.Mode.ANY,  # ANY mode forces the model to predict a function call from a subset of function names.
                allowed_function_names=[],  # Allowed functions to call when mode is ANY, if empty any one of the provided functions will be called.
            )
        )

        # configuring model with the configs and defined tools
        config = GenerationConfig(temperature=0.2)
        self.model = GenerativeModel(
            "gemini-1.5-pro-001",
            tools=[self.tools],
            generation_config=config
        )


    def handle_func_call(self, func_name:str,func_args:dict):
                function_params = {}
                for key in func_args:
                    value = func_args[key]
                    function_params[key] = value

                results = ""

                function_map = {
                    "book_flights": book_flight,
                    "get_search_flights": search_flights,
                    "remove_flight_booking": remove_flight_booking,
                    "update_flight_booking": update_flight_booking,
                    "find_flight_id": find_flight_id,
                    "find_customer_id": find_customer_id,
                    "find_booking_id": find_booking_id,
                }

                function_to_call = function_map.get(func_name)

                if function_to_call:
                    try:
                        print(function_to_call)
                        print(function_params)
                        results = function_to_call(**function_params)
                        print(results)
                        # ... (rest of your result handling code)
                    except Exception as e:
                        return f"Error executing function '{func_name}': {str(e)}"
                else:
                    return f"Error: Unknown function '{func_name}'"
                return results

    def analyze_response(self, response):
        # Check if the response has candidates and content
        parts = response.candidates[0].content.parts
        for part in parts:
            if part.function_call.args:
                return part
        return False  # No function call found


    def handle_response(self, response):  # Pass chat history
        st.write(response)
        output = []
        st.write(response.candidates[0].content.parts)
        part = response.candidates[0].content.parts[0]
        if part.function_call.args:
            function_name = part.function_call.name
            function_args = part.function_call.args

            while True:
                results = self.handle_func_call(func_name=function_name,func_args=function_args)

                if results != "":
                    
                    for content in self.chat.history:
                        print(content.role, "->", [type(part).to_dict(part) for part in content.parts])
                        print("-" * 80)

                    intermediate_response = self.chat.send_message(
                            [
                            Part.from_function_response(
                                name=function_name,
                                response=results
                            )
                        ],)

                    st.write(intermediate_response)
                    analysis = self.analyze_response(intermediate_response)
                    if analysis==False:
                        output.append(intermediate_response.candidates[0].content.parts[0].text)
                        break
                    function_name = analysis.function_call.name
                    function_args = analysis.function_call.args
                    
                else:
                    return "Search Failed"
        else:
            output.append(part.text)
        return output


    def llm_function(self, chat: ChatSession, query):
        response = chat.send_message(query)
        output = self.handle_response(response)  # Pass chat history
        print(output)
        with st.chat_message("model"):
            for o in output:
                st.markdown(o)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": query
            }
        )
        for o in output:
            st.session_state.messages.append(
                {
                    "role": "model",
                    "content": o
                }
            )

    def startAgent(self):
        st.title("Gemini Flights")

        chat = self.model.start_chat(response_validation=False)

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display and load to chat history
        for index, message in enumerate(st.session_state.messages):
            content = Content(
                role=message["role"],
                parts=[Part.from_text(message["content"])]
            )

            if index != 0:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            chat.history.append(content)

        # For Initial message startup
        if len(st.session_state.messages) == 0:
            # Invoke initial message
            initial_prompt = """Introduce yourself as a flights management assistant, ReX, powered by Google Gemini and designed to search/book flights. You use emojis to be interactive. For reference, the year for dates is 2024. """

            self.llm_function(chat, initial_prompt)

        # For capture user input
        query = st.chat_input("Gemini Flights")

        if query:
            with st.chat_message("user"):
                st.markdown(query)
            self.llm_function(chat, query + 
                        """. Use the functional tools provided. When user inquires to make a booking collect the necessary inputs and call the booking tool provided.
                        
        To book a flight, follow these steps:
        1. If the user provides a flight number and departure date, 
        use the 'find_flight_id' tool to get the 'flight_id'.
        2. Use the 'book_flights' tool with the retrieved 'flight_id' and other booking details.

        Be conversational and use emojis! The year for dates is 2024.
        """)


        #export GOOGLE_APPLICATION_CREDENTIALS="/Users/ashadi/Documents/mission-quizify/authentication.json"
