from typing import List
from fastapi import APIRouter, status, Body, Response, Path
from models.User import UserRegister, UserToUpdate, User, UserLogin
from db import database
from time import sleep
from uuid import UUID

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
    # response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
)
def signup(user_data: UserRegister=Body(...)):
    user_password = user_data.dict().get("password")
    user_data.dict().pop("password")
    user = user_data.dict()
    user["user_id"] = str(user["user_id"])
    user["email"] = str(user["email"])
    user["first_name"] = str(user["first_name"])
    user["last_name"] = str(user["last_name"])
    user["birth_date"] = str(user["birth_date"])
    user_password = str(user_password)
    data = db.insertUser(user)
    data.pop("password")
    password_message = db.insertPassword(user_password, user["user_id"])
    return data, password_message

### User login
@router.post(
    path="/login",
    # status_code=status.HTTP_200_OK,
    summary="Login a User"
)
def login(user_data: UserLogin=Body(...), response: Response = None):
    user = user_data.dict()
    user["user_id"] = str(user["user_id"])
    user["email"] = str(user["email"])
    user["password"] = str(user["password"])
    user_signed = db.readRegisterUser(user["user_id"], user["email"], user["password"])
    if (user_signed == None):
        message = {"signup error": "This user does not exist in Database"}
        response.status_code = status.HTTP_403_FORBIDDEN
        return message
    else:
        response.status_code = status.HTTP_200_OK
        return user_signed


### Show all users
@router.get(
    path="/",
    # response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users"
)
def show_all_users():
    data = db.readAllUsers()
    return data


### Show a user
@router.get(
    path="/{user_id}",
    # response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user"
)
def show_a_user(user_id: UUID = Path(
                                    ...,
                                    title="User ID",
                                    description="This is a the user id, it is mandatory"),
                response: Response = None):
    row = db.readUser(user_id)
    print(f">>>  {row}")
    data = {}
    if row is None:
        data[f"{user_id}"]= "HTTP_404_NOT_FOUND"
        response.status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(row, tuple):
        data["email"]= row[0]
        data["user_id"]= row[1]
        data["first_name"]= row[2]
        data["last_name"]= row[3]
        data["birth_date"]= row[4]
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return row

    return data


### Delete a user
@router.post(
    path="/{user_id}/delete",
    # response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User"
)
def delete_a_user(user_id: UUID = Path(
                                    ...,
                                    title="User ID",
                                    description="This is a the user id, it is mandatory"),
                 response: Response = None):
    row = db.readUser(user_id)
    print(f">>>  {row}")
    data = {}
    if row is None:
        data[f"{user_id}"]= "HTTP_404_NOT_FOUND"
        response.status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(row, tuple):
        data["email"]= row[0]
        data["user_id"]= row[1]
        data["first_name"]= row[2]
        data["last_name"]= row[3]
        data["birth_date"]= row[4]
        db.deletePassword(user_id)
        db.deleteUser(user_id)
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return row

    return data


### Update a user
@router.put(
    path="/{user_id}/update",
    # response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User"
)
def update_a_user(user_id: UUID = Path(
                                    ...,
                                    title="User ID",
                                    description="This is a the user id, it is mandatory"),
                 user_data: UserToUpdate = Body(...),
                 response: Response = None):
    row = db.readUser(user_id)
    data={}
    if row is None:       
        data[f"{user_id}"]= "HTTP_404_NOT_FOUND"
        response.status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(row, tuple):
        user_password = user_data.dict().get("password")
        user_data.dict().pop("password")
        row = user_data.dict()
        row["email"] = str(row["email"])
        row["first_name"] = str(row["first_name"])
        row["last_name"] = str(row["last_name"])
        row["birth_date"] = str(row["birth_date"])
        user_password = str(user_password)
        data = db.updateUser(row, user_id)
        update_password_message = db.updatePassword(user_password, user_id)
        response.status_code = status.HTTP_200_OK
        return data, update_password_message
    else:
        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return row

    return data