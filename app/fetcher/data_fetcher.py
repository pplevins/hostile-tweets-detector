from app.fetcher import Database


class DataFetcher:
    def __init__(self, db: Database):
        """Constructor."""
        self.collection = db.get_tweets_collection()

    async def list(self) -> list:
        """List all tweets in the database."""
        return await self.collection.find().to_list()
