import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Tool, Part, Content, ChatSession
from services.flight_manager import search_flights,book_flight,update_flight_booking,remove_flight_booking,find_booking_id,find_customer_id,find_flight_id

from vertexai.preview.generative_models import ToolConfig


project = "trans-array-427509-h2"
vertexai.init(project = project)

#Tool definitions

#tool for searching flights
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
#tool for booking flights
handle_booking_flights = generative_models.FunctionDeclaration(
    name = "book_flights",
    description="This function books seats on a flight identified by its flight_id. It handles seat booking for different classes (economy, business, first class) and calculates the total cost based on the number of seats and the seat type. It updates the flight's seat availability and commits the changes to the database.",
    parameters={
        "type":"object",
        "properties":{
            "first_name":{
                "type":"string",
                "description":"The first name of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "last_name":{
                "type":"string",
                "description":"The last name of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "email":{
                "type":"string",
                "description":"The email of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "phone_number":{
                "type":"integer",
                "description":"The phone number of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "date_of_birth":{
                "type":"string",
                "format":"date",
                "description":"The date of birth of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
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
            "booking_date":{
                "type":"string",
                "format":"date",
                "description":"The date the user makes the flight booking for that is used to create the booking entry in the Booking table along with the other gathered information."
            }
            
        },
        "required":[
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone_number",
            "flight_id",
            "seat_type",
            "num_seats",
            "booking_date"
        ]
      },
    )


#tool for removing previous booking entry
handle_removing_booking = generative_models.FunctionDeclaration(
    name = "remove_flight_booking",
    description="This function is removes previous booking appointments made by the user in the Booking table. The booking_id is used to identify the entry in the Booking table that the user wishes to remove",
    parameters={
        "type":"object",
        "properties":{
          "booking_id":{
            "type":"integer",
            "description":"used to alocate the booking entry that needs to be removed"
          }
        },
        "required":"booking_id"
    }
)

#tool foor update previous or recent booking entry
handle_update_booking = generative_models.FunctionDeclaration(
    name = "update_flight_booking",
    description="This function updates an existing entry in the Booking table of the database with new information that the user provides and new information(new number of seats,new seat type, new flight) calculated by the system(new cost)",
    parameters={
        "type":"object",
        "properties":{
            "booking_id":{
                "type":"integer",
                "description":"Used to alocate the booking entry that needs to be updated"
            },
            "new seat type":{
                "type":"string",
                "description":"states what seat type the customer wants to change the booking entry to."
            },
            "new_num_seats":{
                "type":"integer",
                "description":"states the new number of seats the user wishes to book and update the current booking entry to."
            },
            "new_total_cost":{
                "type":"integer",
                "description":"based on the new seat type and new number of seats requested by the user, this parameter states the new evaluated cost that the user must pay for the booking."
            },
            "flight_id":{
                "type":"integer",
                "description":"The new flight that the user wishes to change to from the previous flight mentioned in the booking entry."
            }
        },
        "required":"booking_id"
    }
)

find_flight_id_funct = generative_models.FunctionDeclaration(
    name = "find_flight_id" , 
    description="This is a helper function used for the fuctions: get_search_flights,book_flights,remove_flight_booking,update_flight_booking. It is used when the functions mentioned require flight_id as an input parameter",
    parameters={
        "type":"object",
        "properties":{
            "flight_number":{
                "type":"integer",
                "description":"This is retrieved from the previous information when the user mentions the flight number in specific mentioned when searching or booking flights."
            },
            "departure_date":{
                "type":"string",
                "format":"date",
                "description":"This is retrieved from the previous information when the user mentions the departure date of the flight during flight search or flight booking."
            }
        },
        "required":["flight_number","departure_date"]
    }
)

find_customer_id_func = generative_models.FunctionDeclaration(
    name = "find_customer_id" , 
    description="This is a helper function used for the fuctions: book_flights,remove_flight_booking,update_flight_booking. It is used when the functions mentioned require customer_id as an input parameter",
    parameters={
        "type":"object",
        "properties":{
            "email":{
                "type":"string",
                "description":"This is retrieved from the previous information when the user mentions their email during booking flights."
            }
        },
        "required":["email"]
    }
)

find_booking_id_func = generative_models.FunctionDeclaration(
     name = "find_booking_id" , 
    description="This is a helper function used for the fuctions: remove_flight_booking,update_flight_booking. It is used when the functions mentioned require flight_id as an input parameter.",
    parameters={
        "type":"object",
        "properties":{
            "flight_id":{
                "type":"integer",
                "description":"This could be retrieved from the helper function 'find_flight_id' ."
            },
            "customer_id":{
                "type":"string",
                "format":"date",
                "description":"This could be retrieved from the helper function 'find_customer_id' ."
            }
        },
        "required":["flight_id","customer_id"]
    }
)




tools = generative_models.Tool(
    function_declarations=[handle_booking_flights,get_search_flights,handle_removing_booking,handle_update_booking,find_booking_id_func,find_customer_id_func,find_flight_id_funct]
)

#tool config used for forced function calling. However, its only used for testing purposes
tool_config = ToolConfig(
    function_calling_config=ToolConfig.FunctionCallingConfig(
        mode=ToolConfig.FunctionCallingConfig.Mode.ANY,  # ANY mode forces the model to predict a function call from a subset of function names.
        allowed_function_names=[],  # Allowed functions to call when mode is ANY, if empty any one of the provided functions will be called.
    )
)

#configuring model with the configs and defined tools
config = generative_models.GenerationConfig(temperature=0.2)
model = GenerativeModel(
    "gemini-1.5-pro-001",
    tools = [tools],
    generation_config=config
)





def handle_response(response):
    st.write(response)
    
    if response.candidates[0].content.parts[0].function_call.args:
        function_name = response.candidates[0].content.parts[0].function_call.name
        function_args = response.candidates[0].content.parts[0].function_call.args

        function_params = {}
        for key in function_args:
            value = function_args[key]
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

        function_to_call = function_map.get(function_name)
 
        if function_to_call:
          try:
            results = function_to_call(**function_params) 

            # ... (rest of your result handling code)

          except Exception as e:
            return f"Error executing function '{function_name}': {str(e)}"
        else:
           return f"Error: Unknown function '{function_name}'" 
  
        
        if results != "":
            intermediate_response = chat.send_message(
                Part.from_function_response(
                    name = function_name,
                    response=results
                )
            )
            st.write(intermediate_response)
            return intermediate_response.candidates[0].content.parts.text
        
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
    llm_function(chat, query + ". Use the functional tools provided. When user inquires to make a booking collect the necessary inputs and call the booking tool provided.")
