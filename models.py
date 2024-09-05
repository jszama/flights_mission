from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from pydantic import BaseModel, Field
from datetime import date, datetime, time
from typing import Optional

DATABASE_URL = "sqlite:///./flights.db"
Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"

    flight_id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, index=True)
    airline = Column(String)
    origin = Column(String)
    destination = Column(String)
    
    departure_date = Column(Date)
    arrival_date = Column(Date)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    
    open_seats_economy = Column(Integer)
    open_seats_business = Column(Integer)
    open_seats_first_class = Column(Integer)
    economy_seat_cost = Column(Integer)
    business_seat_cost = Column(Integer)
    first_class_cost = Column(Integer)

    booking = relationship("Booking",back_populates="flights")

class Customers(Base):
    __tablename__= "customers"

    customer_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String,index=True)
    last_name = Column(String,index=True)
    email = Column(String,unique=True,index=True)
    phone_number = Column(Integer,unique=True)
    date_of_birth = Column(Date)

    booking = relationship("Booking", back_populates="customers")


class Booking(Base):
    __tablename__ = "booking"

    customers = relationship("Customers",back_populates="booking")
    flights = relationship("Flight",back_populates="booking")

    booking_id = Column(Integer,primary_key=True)
    flight_id = Column(Integer,ForeignKey('flights.flight_number'))
    customer_id = Column(Integer,ForeignKey('customers.customer_id'))
    booking_date = Column(Date,default=date.today())
    seat_type = Column(String)
    num_seats = Column(Integer)
    total_cost = Column(Integer)


# Pydantic Models for inputs & Body Validation


#table entry models
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


####

#Input models
    
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
####
# Create the database
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Create a Session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
