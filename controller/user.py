from typing import List
from fastapi import APIRouter, status, Body
from models.User import UserRegister, User
from db import database
from time import sleep


sleep(10)
db = database.Db()
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Path Operations
## Users
## The client will send the information
### Register a user
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup():
    pass

### User login
@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    summary="Login a User"
)
def login(user_data: UserRegister=Body(...)):
    user = user_data.dict()
    user["user_id"] = str(user["user_id"])
    user["email"] = str(user["email"])
    user["first_name"] = str(user["first_name"])
    user["last_name"] = str(user["last_name"])
    user["birth_date"] = str(user["birth_date"])
    user["password"] = str(user["password"])
    data = db.insertUser(user)
    return data

### Show all users
@router.get(
    path="/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass

### Show a user
@router.get(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user():
    pass

### Delete a user
@router.post(
    path="/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass


### Update a user
@router.put(
    path="/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass