from vertexai.preview.generative_models import FunctionDeclaration

# tool for booking flights
handle_booking_flights_func = FunctionDeclaration(
    name="book_flights",
    description="This function books seats on a flight identified by its flight_id. It handles seat booking for different classes (economy, business, first class) and calculates the total cost based on the number of seats and the seat type. It updates the flight's seat availability and commits the changes to the database.",
    parameters={
        "type": "object",
        "properties": {
            "first_name": {
                "type": "string",
                "description": "The first name of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "last_name": {
                "type": "string",
                "description": "The last name of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "email": {
                "type": "string",
                "description": "The email of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "phone_number": {
                "type": "integer",
                "description": "The phone number of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "date_of_birth": {
                "type": "string",
                "format": "date",
                "description": "The date of birth of the user that is making the booking. It is used to update and add the user details in the Customer table of the User database."
            },
            "flight_id": {
                "type": "integer",
                "description": "The unique identifier of the flight to book. You can find flight ID using the find_flight_id tool."
            },
            "seat_type": {
                "type": "string",
                "description": "The class of the seat to book (economy, business, or first_class)."
            },
            "num_seats": {
                "type": "integer",
                "description": "The number of seats to book (default is 1)."
            },
            "booking_date": {
                "type": "string",
                "format": "date",
                "description": "The date the user makes the flight booking for that is used to create the booking entry in the Booking table along with the other gathered information."
            }

        },
        "required": [
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