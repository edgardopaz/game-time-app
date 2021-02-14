import tweepy
from app.nba_data import get_todays_games
from config import Config

CONSUMER_KEY = Config.CONSUMER_KEY
CONSUMER_SECRET = Config.CONSUMER_SECRET
ACCESS_TOKEN = Config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = Config.ACCESS_TOKEN_SECRET


def send_tweet() -> None:
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    api.update_status(get_todays_games())
