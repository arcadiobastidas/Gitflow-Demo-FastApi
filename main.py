from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException

from app.auth import create_access_token, verify_token, hash_password, verify_password
from pydantic import BaseModel

app = FastAPI()


# User login model
class UserLogin(BaseModel):
    username: str
    password: str


# Mock user database (hashed password)
fake_users_db = {
    "futurecore": {"username": "futurecore", "password": hash_password("securepassword")}
}

# quiero saber como se hace esto


# Login endpoint (JWT authentication)
@app.post("/login")
async def login(user: UserLogin):
    # Validate user
    if user.username not in fake_users_db or not verify_password(user.password,
                                                                 fake_users_db[user.username]["password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Generate JWT token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token({"sub": user.username}, access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}


# Secure API endpoint (Requires authentication)
@app.get("/secure-data", dependencies=[Depends(verify_token)])
async def secure_data():
    return {"message": "Secure data accessible"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
