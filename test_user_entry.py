import pytest
from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from models import Customers,CustomerInput
from services.flight_manager import handle_user_data_entry

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
