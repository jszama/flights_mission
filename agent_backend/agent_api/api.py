from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import logging

from services.flight_manager import generate_flights, handle_flight_search, handle_flight_book,remove_booking_entry,update_booking_entry

from database.models.DatabaseModels import Flight, Booking, Customers
from database.models.InputModels import FlightInput, BookFlightInput, FlightSearchCriteria, UpdateBookingInput
from database.models.TableEntryModels import FlightModel, BookingModel, CustomerModel

from database.database import get_db

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
    
app = FastAPI()

@app.post("/generate-flight/")
def generate_flight(flight_input: FlightInput, num_flights: int, db: Session = Depends(get_db)):
    return generate_flights(flight_input, num_flights, db)

@app.post("/book_flight")
def book_flight_endpoint(criteria:BookFlightInput, db: Session = Depends(get_db)):
    try:
        result = handle_flight_book(criteria=criteria,db=db)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/flights/", response_model=List[FlightModel])
def read_all_flights(db: Session = Depends(get_db)):
    flights = db.query(Flight).all()
    return flights

@app.get("/customers/",response_model=List[CustomerModel])
def read_all_customers(db: Session = Depends(get_db)):
   customers = db.query(Customers).all()
   return customers

@app.get("/bookings/",response_model=List[BookingModel])
def read_all_customers(db: Session = Depends(get_db)):
   bookings = db.query(Booking).all()
   return bookings

@app.get("/search-flights/")
def search_flights_endpoint(criteria: FlightSearchCriteria = Depends(), page: Optional[int] = 1, page_size: Optional[int] = 10, db: Session = Depends(get_db)):
    return handle_flight_search(criteria, db, page, page_size)

@app.post("/remove_booking_entry")
def remove_booking_endpoint(booking_id:int, db: Session = Depends(get_db)):
    return remove_booking_entry(booking_id=booking_id , db=db)

@app.post("/update_booking/")
def update_booking_endpoint(criteria:UpdateBookingInput,db:Session=Depends(get_db)):
    return update_booking_entry(criteria,db)

# @app.get("/find_flight_id")
# def find_flight_id_endpoint(criteria:models.findFlightID,db:Session=Depends(models.get_db)):
#     return find_flight_id(criteria,db)