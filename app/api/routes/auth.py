from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.facades.authentication.auth_facade import AuthFacade
from app.schemas import Token, UserLogin

router = APIRouter()

"""
This endpoint is in charge of getting the authentication token for the users.
You'll see the ApiROuter decorator, which is used to define the path for the endpoint by FastAPI.
"""


@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return AuthFacade.login(user, db)
