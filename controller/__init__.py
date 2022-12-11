from fastapi import APIRouter

from .user import router as user_router
from .tweet import router as tweet_router

router = APIRouter(
    prefix="/api",
)

router.include_router(user_router)
router.include_router(tweet_router)