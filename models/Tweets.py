# Python
from uuid import UUID
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# User model
from models.User import User

class Tweets(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_length = 1, 
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)