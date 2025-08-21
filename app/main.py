import uvicorn
from fastapi import FastAPI
from api import router as tweets_router

app = FastAPI(
    title="Tweets processor API",
    summary="A FastAPI backend service that supplying process service to tweets MongoDB collection.",
)

app.include_router(tweets_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
