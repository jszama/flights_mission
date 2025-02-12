from database.models.DatabaseModels import Base 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./flights.db"

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