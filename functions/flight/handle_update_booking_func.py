from vertexai.preview.generative_models import FunctionDeclaration

# tool for update previous or recent booking entry
handle_update_booking_func = FunctionDeclaration(
    name="update_flight_booking",
    description="This function updates an existing entry in the Booking table of the database with new information that the user provides and new information(new number of seats,new seat type, new flight) calculated by the system(new cost)",
    parameters={
        "type": "object",
        "properties": {
            "booking_id": {
                "type": "integer",
                "description": "Used to alocate the booking entry that needs to be updated"
            },
            "new seat type": {
                "type": "string",
                "description": "states what seat type the customer wants to change the booking entry to."
            },
            "new_num_seats": {
                "type": "integer",
                "description": "states the new number of seats the user wishes to book and update the current booking entry to."
            },
            "new_total_cost": {
                "type": "integer",
                "description": "based on the new seat type and new number of seats requested by the user, this parameter states the new evaluated cost that the user must pay for the booking."
            },
            "flight_id": {
                "type": "integer",
                "description": "The new flight that the user wishes to change to from the previous flight mentioned in the booking entry."
            }
        },
        "required": ["booking_id"]
    }
)