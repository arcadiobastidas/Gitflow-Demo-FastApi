from pydantic import BaseModel, EmailStr

"""
Pydantic models are used to define the structure of the data that is being sent to and received from the API.
this minimizes the amount of code that needs to be written to validate and serialize data.
It is an alternative to JsonStringify and other serialization libraries. It makes my code look cleaner and more readable.
"""


# Schema for User Registration
class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str


# Schema for Returning User Info (excluding password)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True  # Enables automatic conversion from SQLAlchemy models


# Schema for Login
class UserLogin(BaseModel):
    username: str
    password: str


# Schema for JWT Token Response
class Token(BaseModel):
    access_token: str
    token_type: str
