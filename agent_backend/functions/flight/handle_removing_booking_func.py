from vertexai.preview.generative_models import FunctionDeclaration

# tool for removing previous booking entry
handle_removing_booking_func = FunctionDeclaration(
    name="remove_flight_booking",
    description="This function is removes previous booking appointments made by the user in the Booking table. The booking_id is used to identify the entry in the Booking table that the user wishes to remove",
    parameters={
        "type": "object",
        "properties": {
            "booking_id": {
                "type": "integer",
                "description": "used to alocate the booking entry that needs to be removed"
            }
        },
        "required": ["booking_id"]
    }
)