from pydantic import BaseModel
from datetime import date, datetime

# Pydantic Models for entries
class CustomerModel(BaseModel):
     customer_id:int
     first_name:str
     last_name:str
     email:str
     phone_number:int
     date_of_birth:date

class BookingModel(BaseModel):
     booking_id:int
     customer_id:int
     flight_id:int
     booking_date:date
     seat_type:str
     num_seats:int
     total_cost:int

class FlightModel(BaseModel):
    flight_id: int
    flight_number: str
    airline: str
    origin: str
    destination: str
    
    departure_date: date
    arrival_date: date
    departure_time: datetime
    arrival_time: datetime
    
    open_seats_economy: int
    open_seats_business: int
    open_seats_first_class: int
    economy_seat_cost: int
    business_seat_cost: int
    first_class_cost: int

    class Config:
        from_attributes = True