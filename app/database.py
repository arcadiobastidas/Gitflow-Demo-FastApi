from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
These are helper functions and classes to interact with the database.
If we want to switch to a different database, we only need to change the database URL in the settings.
for example, to use a PostgreSQL database, we would change the SQLALCHEMY_DATABASE_URL to: //postgresql://user:password@localhost/db

"""

# SQLite Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

# Create Database Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Model for SQLAlchemy Models
Base = declarative_base()


# Function to Get Database Session (Dependency for FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def reset_database():
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)  # Drop existing tables
    print("Tables dropped.")

    print("Creating new tables...")
    Base.metadata.create_all(bind=engine)  # Recreate tables
    print("Database reset successful!")
