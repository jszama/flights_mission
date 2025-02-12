from vertexai.preview.generative_models import FunctionDeclaration

#tool for finding booking_id
find_booking_id_func = FunctionDeclaration(
    name="find_booking_id",
    description="This is a helper function used for the fuctions: remove_flight_booking,update_flight_booking. It is used when the functions mentioned require flight_id as an input parameter.",
    parameters={
        "type": "object",
        "properties": {
            "flight_id": {
                "type": "integer",
                "description": "This could be retrieved from the helper function 'find_flight_id' ."
            },
            "customer_id": {
                "type": "string",
                "format": "date",
                "description": "This could be retrieved from the helper function 'find_customer_id' ."
            }
        },
        "required": ["flight_id", "customer_id"]
    }
)