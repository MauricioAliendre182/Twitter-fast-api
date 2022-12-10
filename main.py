# Python
from uuid import UUID
from datetime import date
from typing import Optional
from wsgiref.validate import validator

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import status


app = FastAPI()


# Defining the models
class UserBase(BaseModel):
    # What should a user have?
    # UUID: Special class of Python to have a unique ID
    user_id: UUID = Field(...)
    email: EmailStr = Field(..., example="example@hotmail.com") 

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$",
        description="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number and one special character.",
    )
class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: date = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None, example='1998-06-23')
    
    @validator('birth_date')  # Aqui está la magia
    def is_over_eighteen(cls, v):
        todays_date = date.today()
        delta = todays_date - v

        if delta.days/365 <= 18:
            raise ValueError('Must be over 18!')
        else:
            return v

class Tweet(BaseModel):
    pass


@app.get(
    path="/",
    status_code=status.HTTP_200_OK
)
def home():
    return {"Twitter API": "Working!"}