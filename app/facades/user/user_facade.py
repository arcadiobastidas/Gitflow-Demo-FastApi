from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas import UserCreate, UserResponse
from app.services.user.user_service import UserService


class UserFacade:

    # UserService is a class that contains the business logic for user management.

    # Register a new user will call the UserService to handle user creation.
    @staticmethod
    def register_user(user: UserCreate, db: Session):
        # Call the UserService to handle user creation
        if UserService.get_user_by_username(db, user.username):
            raise HTTPException(status_code=400, detail="Username already exists")

        new_user = UserService.create_user(db, user)
        return UserResponse(id=new_user.id, username=new_user.username, email=new_user.email)

    # Get user by ID will call the UserService to handle user retrieval.
    @staticmethod
    def get_user_by_id(user_id: int, db: Session):
        user = UserService.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(id=user.id, username=user.username, email=user.email)
