from typing import List
from fastapi import APIRouter, status, Body
from models.Tweets import Tweets
from db import database
from time import sleep

sleep(10)
db = database.Db()
router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"]
)
## Tweets
### Show all Tweets
@router.get(
    path="/",
    response_model=List[Tweets],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
)
def home():
    return {"Twitter API": "Working!"}

### Post a Tweet
@router.post(
    path="/post",
    # response_model=Tweets,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet"
)
def post(tweet_data: Tweets = Body(...)):
    """
    This path operation registers a Tweet in the app

    Parameters:
      - Request body parameter
            - Tweet: Tweets
    Returns a json with tweet information posted
    """
    tweet = tweet_data.dict()
    tweet["tweet_id"] = str(tweet["tweet_id"])
    tweet["content"] = str(tweet["content"])
    tweet["created_at"] = str(tweet["created_at"])
    tweet["update_at"] = str(tweet["update_at"])
    data = db.insertTweet(tweet)
    return data

### Show a Tweet
@router.get(
    path="/{tweet_id}",
    response_model=Tweets,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
)
def show_a_tweet():
    pass

### Delete a Tweet
@router.post(
    path="/{tweet_id}/delete",
    response_model=Tweets,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
)
def delete_a_tweet():
    pass

### Update a Tweet
@router.put(
    path="/{tweet_id}/update",
    response_model=Tweets,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
)
def update_a_tweet():
    pass