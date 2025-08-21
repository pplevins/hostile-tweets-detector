from fastapi import APIRouter

from app.manager import Manager

router = APIRouter(prefix="/tweets", tags=["soldiers"])
manager = Manager()


@router.get(
    "/",
    response_description="process all the tweets.",
)
async def process_tweets():
    return await manager.get_processed_data()
