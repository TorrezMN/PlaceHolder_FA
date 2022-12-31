from faker import Faker
from fastapi import APIRouter, Depends, HTTPException
from schemas.base_schema import API_RESPONSE
import re

fake = Faker()

utilities_router = APIRouter(
    prefix="/utilities",
    tags=["utilities"],
)


@utilities_router.get("/")
def utilities_home():
    API_RESPONSE["data"] = "UTILITIES HOME!"
    return API_RESPONSE


@utilities_router.get("/validate_email/{email}")
def validate_email(email: str):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.fullmatch(regex, email):
        API_RESPONSE["data"] = "VALID EMAIL"
        return API_RESPONSE
    else:
        API_RESPONSE["data"] = "INVALID EMAIL"
        return API_RESPONSE
