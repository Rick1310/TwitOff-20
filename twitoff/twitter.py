"""Retrieve tweets, users, and 
then create embeddings and populate DB"""

import tweepy
import spacy
from.models import DB, Tweet, Userfrom twitoff.models import username

# TODO Create .env file

TWITTER_API_KEY = "XsDEH821yBNk1XFM2ZguIO3O0"
TWITTER_API_SECRET = "KGSNkNHd6gnwXeO1EdKd7Of1v3rmxUVFXJgWA26w2whqiuNadL"
TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
TWITTER = tweepy.API(TWITTER_AUTH)

def add_or_update_user(username):
    twitter_user = TWITTER.get_user(username)
    db_user = (User.query.get(twitter_user.id)) or User(id=twitter_user.id, name=username)
    DB.session.add(db_user)
    
    tweets = twitter_user.timeline(
        count=200, exclude_replies=True, 
        include_rts=False, tweet_mode="extended"
                                  )

    for tweet in Tweet:
        db_tweet = Tweet(id=tweet.id, text=tweet.full_text)
        db_user.tweets.append(db_tweet)

    DB.session.commit()

