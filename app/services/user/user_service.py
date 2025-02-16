from datetime import datetime

from sqlalchemy.orm import Session

from app.auth import hash_password
from app.models.user import User
from app.schemas import UserCreate

"""
This is the service class for the User model. It contains methods to create a new user, get a user by username, get a user by id, and soft delete a user.
We need to add here any other methods that we want to use to interact with the User model.
"""


class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        hashed_password = hash_password(user.password)
        new_user = User(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def soft_delete_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        user.deletion_date = datetime.utcnow()
        db.commit()
        return user
