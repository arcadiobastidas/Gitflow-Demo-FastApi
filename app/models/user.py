from sqlalchemy import Column, String
from app.database import Base
from app.models.base_entity import BaseEntity


# The User model is a subclass of the BaseEntity class.
# It defines the following columns:
# - username: the user's username
# - email: the user's email address
# - password: the user's hashed password
# - first_name: the user's first name
# - last_name: the user's last name
# The username and email columns are unique and indexed.
class User(Base, BaseEntity):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # Hashed password
