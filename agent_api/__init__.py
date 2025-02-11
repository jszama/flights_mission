import random
from datetime import datetime, timedelta

def generate_flight_number():
    # Example: AA342
    return f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(100, 999)}"


def choose_airline():
    # Example airlines
    airlines = ['Phantom', 'DreamSky Airlines', 'VirtualJet', 'Enchanted Air', 'AeroFiction']
    return random.choice(airlines)


def calculate_times(origin, destination, flight_date):
    # Randomly generate departure time between 0 and 23 hours
    departure_hour = random.randint(0, 23)
    departure_minute = random.randint(0, 59)
    # Use flight_date instead of datetime.now()
    departure_time = datetime.combine(flight_date, datetime.min.time()).replace(hour=departure_hour,
                                                                                   minute=departure_minute)

    # Random duration for the flight between 30 mins to 10 hours
    duration = timedelta(minutes=random.randint(30, 600))
    arrival_time = departure_time + duration

    # Extracting the arrival date
    arrival_date = arrival_time.date()

    return departure_time, arrival_time, arrival_date