from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas import UserLogin, Token
from app.services.authentication.auth_service import AuthService


class AuthFacade:

    # AuthService is a class that contains the business logic for user authentication.
    @staticmethod
    def login(user: UserLogin, db: Session) -> Token:
        # Validate user credentials
        db_user = AuthService.authenticate_user(db, user.username, user.password)
        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        # Generate JWT token
        access_token = AuthService.create_access_token({"sub": db_user.username})

        return Token(access_token=access_token, token_type="bearer")
