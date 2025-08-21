import os
from collections import Counter

import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from app.fetcher import WeaponsFetcher


class DataProcessor:
    def __init__(self):
        nltk_dir = "/tmp/nltk_data"
        os.makedirs(nltk_dir, exist_ok=True)
        nltk.data.path.append(nltk_dir)
        nltk.download('vader_lexicon', download_dir=nltk_dir, quiet=True)  # Compute sentiment labels
        self.raw_data = None
        self.processed_data = None
        self.weapons_list = WeaponsFetcher.fetch_weapons_list()

    def _find_rarest_word(self, tweet_words: list) -> str:
        return Counter(tweet_words).most_common()[-1][0]

    def _calculate_text_sentiment(self, tweet_text: str) -> str:
        compound = SentimentIntensityAnalyzer().polarity_scores(tweet_text).get('compound')
        return "positive" if compound > 0.5 \
            else "negative" if compound < -0.5 else "neutral"

    def _find_weapons(self, tweet_text: str) -> str | None:
        for weapon in self.weapons_list:
            if weapon in tweet_text:
                return weapon
        return None

    def set_data(self, raw_data: pd.DataFrame) -> None:
        self.raw_data = raw_data
        self.raw_data['_id'] = self.raw_data['_id'].apply(lambda x: str(x))
        self.processed_data = raw_data.copy()
        self.processed_data['lower_words'] = (self.processed_data['Text']
                                              .str.replace(r'[^\w\s]+', '', regex=True)
                                              .str.lower()
                                              .str.split(r'\s+'))

    def set_rarest_word_tweets(self):
        self.processed_data['rarest_word'] = self.processed_data['lower_words'].apply(
            lambda x: self._find_rarest_word(x))

    def set_weapon_tweets(self):
        self.processed_data['weapons_detected'] = self.processed_data['Text'].apply(
            lambda x: self._find_weapons(x.lower()))

    def set_sentiment(self):
        self.processed_data['sentiment'] = self.processed_data['Text'].apply(
            lambda x: self._calculate_text_sentiment(x))

    def clean_and_export_data(self):
        self.processed_data = self.processed_data.drop(columns=['lower_words'])
        self.processed_data = self.processed_data.rename(columns={'_id': 'id', 'Text': 'original_text'})
        return self.processed_data.to_dict('records')
