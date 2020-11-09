"""MAin app routing for TwitOff"""

from flask import Flask, render_template

def create_app():
    """Creating and configuring an instance of the flask application"""

    app = Flask(__name__)

    
    # This is a decorator. Is used to add functionality within a function and return it. 
    # @app.route sets the base URL for our app. 
    @app.route('/')
    def root():
        return render_template('base.html', title="home")


    return app

