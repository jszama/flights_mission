import pytest
from sqlalchemy.orm import Session
import sys
import os
from datetime import datetime, timedelta, time, date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from models import SessionLocal, Customers, CustomerInput,BookingInput,Booking,Flight,BookFlightInput
from services.flight_manager import handle_user_data_entry,handle_booking_entry,handle_flight_book

customer1 = CustomerInput(
    first_name="Ashadi",
    last_name="De Silva",
    email="methasa@gmail.com",
    phone_number=111,
    date_of_birth="2005-08-17"
)
customer2 = CustomerInput(
    first_name="Sanuthi",
    last_name="De Silva",
    email ="sanuthi@gmail.com",
    phone_number=222,
    date_of_birth="2008-08-17"
)

booking = BookingInput(
    flight_id=1,
    customer_id=2,
    booking_date="2024-08-21",
    seat_type="economy",
    total_cost=200,
    num_seats=2
)

flight_booking = BookFlightInput(
    first_name="Ashadi",
    last_name="De Silva",
    email="methasa@gmail.com",
    phone_number=111,
    date_of_birth="2005-08-17",
    flight_id=1,
    booking_date="2024-08-21",
    seat_type="economy",
    total_cost=200,
    num_seats=2
)


def create_flight(db:Session):
  db.query(Flight).delete()
  flight = Flight(
            flight_id = 1,
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
            economy_seat_cost=100,
            business_seat_cost=800,
            first_class_cost=1500)
  db.add(flight)
  db.commit()


@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture(autouse=True)
def run_around_tests(db_session):
    # Clean up before each test to ensure isolation
    db_session.query(Customers).delete()
    db_session.query(Booking).delete()
    db_session.commit()
    yield
    # Optional: You can clean up after each test if necessary
    db_session.query(Customers).delete()
    db_session.query(Booking).delete()
    db_session.commit()

def test_handle_user_entry(db_session: Session):
    # Run the function under test with an user already existing in the database
    db_user_entry1 = handle_user_data_entry(customer1, db_session)
    
    # Check that the user was successfully added
    assert db_user_entry1 == True

    # Fetch the user from the database
    user_info1 = db_session.query(Customers).filter_by(email=customer1.email).first()
    
    #Verify the user data
    assert user_info1.first_name == "Ashadi"
    assert user_info1.last_name == "De Silva"
    assert user_info1.email == "methasa@gmail.com"
    assert user_info1.phone_number ==111
    assert str(user_info1.date_of_birth) == "2005-08-17"

    
    # #Run the function under test with a new user
    # db_user_entry2 = handle_user_data_entry(customer2,db_session)
    # assert db_user_entry2 == True
    # # Fetch the user from the database
    # user_info = db_session.query(Customers).filter_by(email=customer2.email).first()
    
    # # Verify the user data
    # assert user_info.first_name == "Sanuthi"
    # assert user_info.last_name == "De Silva"
    # assert user_info.email == "sanuthi@gmail.com"
    # assert user_info.phone_number == 222
    # assert str(user_info.date_of_birth) == "2008-08-17"

def test_handle_booking_entry(db_session:Session):
    db_booking_entry = handle_booking_entry(booking,db_session)
    assert db_booking_entry == True
    booking_info = db_session.query(Booking).filter( Booking.customer_id == booking.customer_id).first()

    assert booking_info.flight_id==1
    assert str(booking_info.booking_date)=="2024-08-21"
    assert booking_info.seat_type=="economy"
    assert booking_info.num_seats==2
    assert booking_info.total_cost==200

def test_handle_booking(db_session:Session):
    create_flight(db_session)
    handle_flight_book(criteria=flight_booking,db=db_session)

    user_info = db_session.query(Customers).filter_by(email=customer1.email).first()
    
    #Verify the user data
    assert user_info.first_name == "Ashadi"
    assert user_info.last_name == "De Silva"
    assert user_info.email == "methasa@gmail.com"
    assert user_info.phone_number ==111
    assert str(user_info.date_of_birth) == "2005-08-17"

    booking_info = db_session.query(Booking).filter(Booking.customer_id == user_info.customer_id).first()

    assert booking_info.flight_id==1
    assert str(booking_info.booking_date)=="2024-08-21"
    assert booking_info.seat_type=="economy"
    assert booking_info.num_seats==2
    assert booking_info.total_cost==200

    flight_info = db_session.query(Flight).filter(Flight.flight_id==1).first()
    assert flight_info.open_seats_economy == 98
    