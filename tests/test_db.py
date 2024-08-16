import pytest
from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from models import Customers,CustomerInput
from services.flight_manager import handle_user_data_entry,update_associate_table,handle_booking_entry

# Mock Criteria class for user data
class MockCriteria:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

@pytest.fixture
def mock_db_session():
    # Create a mock for the database session
    return MagicMock(spec=Session)

def test_handle_user_data_entry_user_exists(mock_db_session):
    # Setup: Mock criteria and query to return an existing user
    criteria = MockCriteria("John", "Doe", "john@example.com", "1234567890")

    # Mock the query behavior
    mock_query = mock_db_session.query.return_value
    mock_query.filter.return_value.count.return_value = 1  # Simulate user already exists
    
    # Call the method
    result = handle_user_data_entry(criteria, mock_db_session)

    # Assert: Ensure that no user is added and no database commit occurs
    assert result is None
    mock_db_session.add.assert_not_called()
    mock_db_session.commit.assert_not_called()

def test_handle_user_data_entry_new_user(mock_db_session):
    # Setup: Mock criteria and query to simulate that the user does not exist
    criteria = MockCriteria("Jane", "Smith", "jane@example.com", "0987654321")

    # Mock the query behavior
    mock_query = mock_db_session.query.return_value
    mock_query.filter.return_value.count.return_value = 0  # Simulate user does not exist

    # Mock adding a new user
    mock_db_session.add.return_value = None  # Mock the behavior of adding a user
    mock_db_session.commit.return_value = None  # Mock the commit action

    # Call the method
    result = handle_user_data_entry(criteria, mock_db_session)

    # Assert: Ensure that the user is added and committed
    assert result is True
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()

def test_handle_user_data_entry_exception_handling(mock_db_session):
    # Setup: Mock criteria and query to simulate that the user does not exist
    criteria = MockCriteria("Emily", "Jones", "emily@example.com", "1122334455")

    # Simulate an exception during the commit operation
    mock_query = mock_db_session.query.return_value
    mock_query.filter.return_value.count.return_value = 0  # Simulate user does not exist

    mock_db_session.commit.side_effect = Exception("Database commit failed")  # Simulate an exception

    # Call the method
    with pytest.raises(Exception):
        handle_user_data_entry(criteria, mock_db_session)

    # Assert: Ensure that the exception is raised and commit was called
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()


import pytest
from unittest.mock import MagicMock
from datetime import datetime

# Assuming `update_associate_table` and `handle_booking_entry` methods are imported from your module

# Mock criteria input object for update_associate_table
class MockBookingCriteria:
    def __init__(self, flight_id, customer_id, booking_id, num_seats=None, total_cost=None, booking_date=None, seat_type=None):
        self.flight_id = flight_id
        self.customer_id = customer_id
        self.booking_id = booking_id
        self.num_seats = num_seats
        self.total_cost = total_cost
        self.booking_date = booking_date
        self.seat_type = seat_type

class MockAssociateTableCriteria:
    def __init__(self,flight_id,customer_id,booking_id):
        self.flight_id = flight_id
        self.customer_id=customer_id
        self.booking_id = booking_id

@pytest.fixture
def mock_db_session():
    # Create a mock database session object
    db_session = MagicMock()
    return db_session

def test_update_associate_table(mock_db_session):
    # Arrange
    criteria = MockAssociateTableCriteria(flight_id=1, customer_id=2, booking_id=3)

    # Act
    result = update_associate_table(criteria, mock_db_session)

    # Assert
    # Check if a new entry was added to the session and committed
    assert result is True
    assert mock_db_session.add.called_once()
    assert mock_db_session.commit.called_once()
    assert mock_db_session.refresh.called_once()

    # Check if the entry was added with the correct values
    new_entry = mock_db_session.add.call_args[0][0]
    assert new_entry.flight_id == criteria.flight_id
    assert new_entry.customer_id == criteria.customer_id
    assert new_entry.booking_id == criteria.booking_id


def test_handle_booking_entry(mock_db_session):
    # Arrange
    booking_date = datetime.now()
    criteria = MockBookingCriteria(
        flight_id=1, 
        customer_id=2, 
        booking_id=3, 
        num_seats=2, 
        total_cost=500.0, 
        booking_date=booking_date, 
        seat_type='economy'
    )

    # Act
    result = handle_booking_entry(criteria, mock_db_session)

    # Assert
    # Check if a new booking entry was added to the session and committed
    assert result is True
    assert mock_db_session.add.called_once()
    assert mock_db_session.commit.called_once()
    assert mock_db_session.refresh.called_once()

    # Check if the booking entry was added with the correct values
    new_booking_entry = mock_db_session.add.call_args[0][0]
    assert new_booking_entry.customer_id == criteria.customer_id
    assert new_booking_entry.flight_id == criteria.flight_id
    assert new_booking_entry.num_seats == criteria.num_seats
    assert new_booking_entry.total_cost == criteria.total_cost
    assert new_booking_entry.booking_date == criteria.booking_date
    assert new_booking_entry.seat_type == criteria.seat_type
