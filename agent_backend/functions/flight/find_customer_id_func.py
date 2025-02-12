from vertexai.preview.generative_models import FunctionDeclaration

#tool for finding customer_id
find_customer_id_func = FunctionDeclaration(
    name="find_customer_id",
    description="This is a helper function used for the fuctions: book_flights,remove_flight_booking,update_flight_booking. It is used when the functions mentioned require customer_id as an input parameter",
    parameters={
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "This is retrieved from the previous information when the user mentions their email during booking flights."
            }
        },
        "required": ["email"]
    }
)
