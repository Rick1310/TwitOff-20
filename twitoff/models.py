"""SQLalchemy models and utility functions for TwitOff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class user(DB.Model):
    """Twitter User Table that will correspond to twets - SQLAlchemy syntax"""
    id = DB.Column(DB.BigInteger, primary_key =True) # id column (primary key)
    name = DB.Column(DB.String, nullable=false )

    def __repr__(self):
        return "<User: {}>".format(self.name)
        







