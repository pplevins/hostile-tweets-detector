from app.fetcher import DataFetcher, Database
from app.processor import DataProcessor

import pandas as pd


class Manager:
    def __init__(self):
        self.fetcher = DataFetcher(Database())
        self.processor = DataProcessor()

    async def get_processed_data(self):
        tweets_list = await self.fetcher.list()
        self.processor.set_data(pd.DataFrame(tweets_list))
        self.processor.set_rarest_word_tweets()
        self.processor.set_sentiment()
        self.processor.set_weapon_tweets()
        return self.processor.clean_and_export_data()
