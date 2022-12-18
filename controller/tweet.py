from typing import List
from uuid import UUID
from fastapi import APIRouter, status, Body, Path, Response
from models.Tweets import Tweets, TweetsToUpdate
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
    # response_model=List[Tweets],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
)
def home():
    data = db.readAllTweets()
    return data

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
    uuid = tweet["by"].get("user_id")
    data = db.insertTweet(tweet, uuid)
    return data

### Show a Tweet
@router.get(
    path="/{tweet_id}",
    # response_model=Tweets,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
)
def show_a_tweet(tweet_id: UUID = Path(
                                    ...,
                                    title="Tweet ID",
                                    description="This is a the tweet id, it is mandatory"),
                response: Response = None):
    row = db.readTweet(tweet_id)
    print(f">>>  {row}")
    data = {}
    if row is None:
        data[f"{tweet_id}"]= "HTTP_404_NOT_FOUND"
        response.status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(row, tuple):
        data["tweet_id"]= row[0]
        data["content"]= row[1]
        data["created_at"]= row[2]
        data["update_at"]= row[3]
        data["user_id"] = row[4]
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return row

    return data

### Delete a Tweet
@router.post(
    path="/{tweet_id}/delete",
    # response_model=Tweets,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
)
def delete_a_tweet(tweet_id: UUID = Path(
                                    ...,
                                    title="Tweet ID",
                                    description="This is a the tweet id, it is mandatory"),
                 response: Response = None):
    row = db.readTweet(tweet_id)
    print(f">>>  {row}")
    data = {}
    if row is None:
        data[f"{tweet_id}"]= "HTTP_404_NOT_FOUND"
        response.status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(row, tuple):
        data["tweet_id"]= row[0]
        data["content"]= row[1]
        data["created_at"]= row[2]
        data["update_at"]= row[3]
        data["user_id"] = row[4]
        db.deleteTweet(tweet_id)
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return row

    return data

### Update a Tweet
@router.put(
    path="/{tweet_id}/update",
    # response_model=Tweets,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
)
def update_a_tweet(tweet_id: UUID = Path(
                                    ...,
                                    title="User ID",
                                    description="This is a the user id, it is mandatory"),
                  tweet_data: TweetsToUpdate = Body(...),
                  response: Response = None):
    row = db.readTweet(tweet_id)
    data={}
    if row is None:       
        data[f"{tweet_id}"]= "HTTP_404_NOT_FOUND"
        response.status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(row, tuple):
        data = tweet_data.dict()
        # data["content"]= row[1]
        # data["created_at"]= row[2]
        # data["update_at"]= row[3]
        db.updateTweet(data, tweet_id)
        response.status_code = status.HTTP_200_OK
        return data
    else:
        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return row

    return data