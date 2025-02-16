from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import verify_token
from app.database import get_db
from app.facades.user.user_facade import UserFacade
from app.schemas import UserCreate, UserResponse

router = APIRouter()


#  Register new user
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserFacade.register_user(user, db)


# Get user by ID (Authenticated)
@router.get("/users/{user_id}", response_model=UserResponse, dependencies=[Depends(verify_token)])
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserFacade.get_user_by_id(user_id, db)
