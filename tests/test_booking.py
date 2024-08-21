import unittest
from unittest.mock import MagicMock
from datetime import datetime
from sqlalchemy.orm import Session

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from services.flight_manager import handle_flight_book
from models import BookFlightInput, Flight, Customers, Booking  # Replace with actual module name

class TestBookFlight(unittest.TestCase):

    def setUp(self):
        # Create a mock database session
        self.db = MagicMock(spec=Session)

        # Set up mock flight data
        self.flight = Flight(
            flight_id=1,
            airline="Phantom",
            origin="New York",
            destination="Los Angeles",
            departure_date=datetime(2024, 8, 15).date(),
            arrival_date=datetime(2024, 8, 15).date(),
            departure_time=datetime(2024, 8, 15, 14, 0),
            arrival_time=datetime(2024, 8, 15, 17, 0),
            open_seats_economy=100,
            open_seats_business=50,
            open_seats_first_class=20,
            economy_seat_cost=200,
            business_seat_cost=800,
            first_class_cost=1500
        )
        self.db.query(Flight).filter.return_value.first.return_value = self.flight

        # Set up mock customer data
        self.customer = Customers(
            customer_id=1,
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            date_of_birth=datetime(1990, 1, 1).date()
        )
        self.db.query(Customers).filter.return_value.first.return_value = self.customer

    def test_successful_booking(self):
        # Set up the input data for booking
        params = {
            "first_name":"John",
            "last_name":"Doe",
            "email":"johndoe@example.com",
            "phone_number":1234567899,
            "date_of_birth":"1990-01-01",
            "flight_id":1,
            "seat_type":"economy",
            "booking_date":"2024-08-10",
            "num_seats":2
        }
        booking_input = BookFlightInput(**params)
        # Call the function to test
        response = handle_flight_book(criteria=booking_input, db=self.db)

        # Verify the flight was updated correctly
        self.assertEqual(self.flight.open_seats_economy, 98)  # 2 seats booked
        self.assertIn("Successfully booked", response['message'])

    def test_booking_failure_no_seats(self):
        # Set up the input data for booking
        self.flight.open_seats_economy = 1  # Only 1 seat available

        booking_input = BookFlightInput(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            date_of_birth="1990-01-01",
            flight_id=1,
            seat_type="economy",
            booking_date="2024-08-10",
            num_seats=2
        )

        # Call the function to test
        response = handle_flight_book(criteria=booking_input, db=self.db)

        # Verify the failure message
        self.assertEqual(response, "Not enough economy seats available.")

    def test_booking_failure_flight_not_found(self):
        # No flight found for the given flight_id
        self.db.query(Flight).filter.return_value.first.return_value = None

        booking_input = BookFlightInput(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            date_of_birth="1990-01-01",
            flight_id=999,  # Invalid flight_id
            seat_type="economy",
            booking_date="2024-08-10",
            num_seats=1
        )

        # Call the function to test
        response = handle_flight_book(criteria=booking_input, db=self.db)

        # Verify the failure message
        self.assertEqual(response, "Flight not found.")

if __name__ == '__main__':
    unittest.main()
