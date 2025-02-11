from sqlalchemy import Column, Integer, String, DateTime, Date,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import date

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

