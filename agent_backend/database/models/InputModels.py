from datetime import date, time
from pydantic import BaseModel
from typing import Optional

# Pydantic Models for inputs
class BookingInput(BaseModel):
    flight_id: int
    customer_id : int
    booking_date : date
    seat_type : str
    num_seats : int
    total_cost : int
    class Config:
        from_attributes = True

class CustomerInput(BaseModel):
    first_name : str
    last_name : str
    email : str
    phone_number : int
    date_of_birth : date


class FlightInput(BaseModel):
    origin: str
    destination: str
    departure_date: date

class SeatInput(BaseModel):
     flight_id:int
     num_seats:int
     seat_type:str

#Flight search input model
class FlightSearchCriteria(BaseModel):
    origin: str
    destination: str
    departure_date: date
    arrival_date: Optional[str] = None
    flight_number: Optional[str] = None
    airline: Optional[str] = None
    departure_time: Optional[time] = None
    arrival_time: Optional[time] = None
    seat_type: Optional[str] = None  # 'economy', 'business', 'first_class'
    min_cost: Optional[int] = None
    max_cost: Optional[int] = None

#flight booking input model
class BookFlightInput(BaseModel):
                       first_name:str
                       last_name:str
                       email:str
                       phone_number:int
                       date_of_birth:date
                       flight_id: int
                       seat_type: str
                       booking_date:date = date.today()
                       num_seats: int = 1

#Booking update input model
class UpdateBookingInput(BaseModel):
     booking_id:int
     new_seat_type:Optional[str]
     new_num_seats:Optional[int]
     new_total_cost:Optional[int]
     new_flight_id:Optional[int]

#Removing a booking entry
class RemoveBookingInput(BaseModel):
     booking_id:int
     
class findFlightID(BaseModel):
     flight_number:int
     departure_date:date