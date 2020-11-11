"""Retrieve tweets, users, and 
then create embeddings and populate DB"""

import spacy
import tweepy
from.models import DB, Tweet, User
from os import getenv

# TODO Create .env file

TWITTER_API_KEY = "XsDEH821yBNk1XFM2ZguIO3O0"
TWITTER_API_SECRET = "KGSNkNHd6gnwXeO1EdKd7Of1v3rmxUVFXJgWA26w2whqiuNadL"
TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
TWITTER = tweepy.API(TWITTER_AUTH)

# NLP model

nlp = spacy.load('my_model')

def vectorize_twet(tweet_text):
    return nlp(tweet_text).vector

def add_or_update_user(username):
    twitter_user = TWITTER.get_user(username)
    db_user = (User.query.get(twitter_user.id)) or User(id=twitter_user.id, name=username)
    DB.session.add(db_user)

    # Pulls tweets from twitter_user.
    tweets = twitter_user.timeline(
        count = 200, 
        exclude_replies = True, 
        include_rts = False, 
        tweet_mode = "extended",
        since_id = db_user.newest_tweet_id 
                                  )

    # Adds newest tweet to db_user.newest_tweet_id
    if tweets:
        db_user.newest_tweet_id = tweets[0].id

    for tweet in tweets:
        # Stores numerical representations
        vectorized_tweet = vectorize_tweet(tweet.full_text)
        db_tweet = Tweet(id=tweet.id, text=tweet.full_text,
                         vect = vectorized_tweet)
        db_user.tweets.append(db_tweet)
        DB.session.add(db_tweet)

    except Exception as e:
        # Prints and displays error to user and raises throughout app
        print('Error processing'{}: {}.format(username, e))
        raise e
    # Commits changes after tyhe previous try has completed. 
        else:
    DB.session.commit()

    def update_all_users():
         """Update all tweets from all users in the Users table."""
         for user in User.query.all()
         add_or_update_user(user.name)


  

