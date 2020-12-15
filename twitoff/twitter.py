"""Retrieve tweets, users, and 
then create embeddings and populate DB"""

import spacy
import tweepy
from.models import DB, Tweet, User
from os import getenv


TWITTER_AUTH = tweepy.OAuthHandler(
    getenv("TWITTER_API_KEY"), getenv("TWITTER_API_KEY_SECRET"))
TWITTER = tweepy.API(TWITTER_AUTH)  

# nlp model
nlp = spacy.load('my_model')


def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector


def add_or_update_user(username):
    try:
        # grabs user with username from twitter DB
        twitter_user = TWITTER.get_user(username)
        # adds or updates user
        #TODO Research logical or, and, if statements.
        db_user = (User.query.get(twitter_user.id)) or User(
            id=twitter_user.id, name=username)
        DB.session.add(db_user)

        # grabs tweets from twitter_user
        tweets = twitter_user.timeline(
            count=200, 
            exclude_replies=True, 
            include_rts=False,
            tweet_mode="extended", 
            since_id=db_user.newest_tweet_id
        )

        # adds newest tweet to db_user.newest_tweet_id
        if tweets:
            db_user.newest_tweet_id = tweets[0].id

        for tweet in tweets:
            # stores numerical representations
            vectorized_tweet = vectorize_tweet(tweet.full_text)
            db_tweet = Tweet(id=tweet.id, 
                             text=tweet.full_text,
                             vect=vectorized_tweet)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)

    except Exception as e:
        # prints error to user and raises throughout app
        print('Error processing{}: {}'.format(username, e))
        raise e

    # commits changes after try has completed
    else:
        DB.session.commit()


def update_all_users():
    """Update all Tweets for all Users in the User table."""
    for user in User.query.all():
        add_or_update_user(user.name)


  

