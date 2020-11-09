"""MAin app routing for TwitOff"""

from flask import Flask

def create_app():
    app = Flask(__name__)

    
    # This is a decorator. Is used to add functionality within a function and return it. 
    # @app.route sets the base URL for our app. 
    @app.route('/')
    def root():
        return "Hello, Twitoff!"


    return app

