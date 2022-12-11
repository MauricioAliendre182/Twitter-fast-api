# Python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List

# DB
from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import validator

# FastAPI
from fastapi import FastAPI
from fastapi import status


app = FastAPI()


# Defining the models
class UserBase(BaseModel):
    __tablename__ = "UserBase",
    # What should a user have?
    # UUID: Special class of Python to have a unique ID
    user_id: UUID = Field(...)
    email: EmailStr = Field(..., example="example@hotmail.com") 

class UserLogin(UserBase):
    __tablename__ = "UserLogin"
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$",
        description="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number and one special character.",
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
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
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_length = 1, 
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path Operations
@app.get(
    path="/",
    status_code=status.HTTP_200_OK
)
def home():
    return {"Twitter API": "Working!"}
## Users
## The client will send the information
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

@app.post(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user():
    pass

@app.post(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass

## Tweets
@app.get(
    path="/",
    status_code=status.HTTP_200_OK
)
def home():
    return {"Twitter API": "Working!"}