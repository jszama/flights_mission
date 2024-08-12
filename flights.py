import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Tool, Part, Content, ChatSession
from services.flight_manager import search_flights,book_flight

project = "trans-array-427509-h2"
vertexai.init(project = project)

# Define Tool
get_search_flights = generative_models.FunctionDeclaration(
    name="get_search_flights",
    description="Tool for searching a flight with origin, destination, and departure date",
    parameters={
        "type": "object",
        "properties": {
            "origin": {
                "type": "string",
                "description": "The airport of departure for the flight given in airport code such as LAX, SFO, BOS, etc."
            },
            "destination": {
                "type": "string",
                "description": "The airport of destination for the flight given in airport code such as LAX, SFO, BOS, etc."
            },
            "departure_date": {
                "type": "string",
                "format": "date",
                "description": "The date of departure for the flight in YYYY-MM-DD format"
            },
        },
        "required": [
            "origin",
            "destination",
            "departure_date"
        ]
    },
)

handle_booking_flights = generative_models.FunctionDeclaration(
    name = "book_flights",
    description="This function books seats on a flight identified by its flight_id. It handles seat booking for different classes (economy, business, first class) and calculates the total cost based on the number of seats and the seat type. It updates the flight's seat availability and commits the changes to the database.",
    parameters={
        "type":"object",
        "properties":{
            "flight_id":{
                "type":"integer",
                "description": "The unique identifier of the flight to book."
            },
            "seat_type":{
                "type":"string",
                "description": "The class of the seat to book (economy, business, or first_class)."
            },
            "num_seats":{
                "type":"integer",
                "description":"The number of seats to book (default is 1)."
            },
        },
        "required":[
            "flight_id",
            "seat_type",
            "num_seats",
        ]
      },
    )

tools = generative_models.Tool(
    function_declarations=[handle_booking_flights,get_search_flights]
)

config = generative_models.GenerationConfig(temperature=0.4)
model = GenerativeModel(
    "gemini-pro",
    tools = [tools],
    generation_config=config
)

def handle_response(response):
    if response.candidates[0].content.parts[0].function_call.args:
        function_name = response.candidates[0].content.parts[0].function_call.name
        function_args = response.candidates[0].content.parts[0].function_call.args

        function_params = {}
        for key in function_args:
            value = function_args[key]
            function_params[key] = value

        results = ""

        if function_name == "book_flights":
            results = book_flight(**function_args)
        elif function_name =="get_search_flights":
            results = search_flights(**function_params)
        
        if results != "":
            intermediate_response = chat.send_message(
                Part.from_function_response(
                    name = function_name,
                    response=results
                )
            )
            return intermediate_response.candidates[0].content.parts[0].text
        
        else:
            return "Search Failed"
    else:
        return response.candidates[0].content.parts[0].text
    
def llm_function(chat:ChatSession,query):
    response = chat.send_message(query)
    output = handle_response(response)

    with st.chat_message("model"):
       st.markdown(output)
    
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )

st.title("Gemini Flights")

chat = model.start_chat()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display and load to chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(
            role = message["role"],
            parts = [ Part.from_text(message["content"]) ]
        )
    
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    chat.history.append(content)

# For Initial message startup
if len(st.session_state.messages) == 0:
    # Invoke initial message
    initial_prompt = "Introduce yourself as a flights management assistant, ReX, powered by Google Gemini and designed to search/book flights. You use emojis to be interactive. For reference, the year for dates is 2024"

    llm_function(chat, initial_prompt)

# For capture user input
query = st.chat_input("Gemini Flights")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)
