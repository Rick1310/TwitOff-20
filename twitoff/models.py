"""SQLalchemy models and utility functions for TwitOff"""


from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()

# Using SQLalchemy, we can populate tables, columns, etc. 
# As well as populating data within.

# User table
class User(DB.Model):
    """Twitter User Table that will correspond to tweets - SQLAlchemy syntax"""
    # The same information needed to create tables in a standard SQL query are needed
    # and passed in as args. 
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column (primary key)
    name = DB.Column(DB.String, nullable=False)  # name column
    newest_tweet_id = DB.Column(DB.BigInteger) # Keeps track of most recent tweet.

    # __repr__ indicates string representation of the class object. 
    #TODO Research __repr__ var
    def __repr__(self):
        return "<User: {}>".format(self.name)



# Twitter table
class Tweet(DB.Model):
    """Tweet text data - associated with Users Table"""
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column (primary key)
    text = DB.Column(DB.Unicode(300)) # Text of the tweet
    vect = DB.Column(DB.PickleType, nullable=False) 
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False) 
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

def __repr__(self):
    return "<tweet: {}>".format(self.text)
