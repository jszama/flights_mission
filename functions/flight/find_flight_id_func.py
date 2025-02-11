from vertexai.preview.generative_models import FunctionDeclaration

#tool for finding flight_id
find_flight_id_func = FunctionDeclaration(
    name="find_flight_id",
    description="This is a helper function used for the functions: get_search_flights,book_flights,remove_flight_booking,update_flight_booking. It is used when the functions mentioned require flight_id as an input parameter",
    parameters={
        "type": "object",
        "properties": {
            "flight_number": {
                "type": "string",
                "description": "This is retrieved from the previous information when the user mentions the flight number in specific mentioned when searching or booking flights.The flight number is a commbination of letters and integers"
            },
            "departure_date": {
                "type": "string",
                "format": "date",
                "description": "This is retrieved from the previous information when the user mentions the departure date of the flight during flight search or flight booking."
            }
        },
        "required": ["flight_number", "departure_date"]
    }
)

