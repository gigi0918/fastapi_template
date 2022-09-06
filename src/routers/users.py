from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.functions import userFunc

router = APIRouter()

# http://127.0.0.1:8000/v1/users/test 
@router.get("/testGet")
async def get_users():
    return userFunc.get_user()
    

@router.get("/testError")
async def read_user_me():
    raise HTTPException(
            status_code=418, detail="ERROR DETAIL"
        )

@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}


class User(BaseModel):
    username: str
    phone_number: Optional[str] = None
    email: Optional[str] = None

@router.post("/testPost")
async def read_user(user: User):
    return {"username": user.username, "details": user}
