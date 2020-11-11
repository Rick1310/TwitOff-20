from os import getenv
from flask import Flask, render_template, request
from .models import DB, User 
from .twitter import add_or_update_user




# creates application
def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    # database and app configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initilizing database
    DB.init_app(app)

    # decorator listens for specific endpoint visits
    @app.route('/')  # http://127.0.0.1:5000/
    def root():
        # renders base.html template and passes down title and users
        return render_template('base.html', title="home", users=User.query.all())

        @app.route('/compare', methods=["POST"]) # http://127.0.0.1:5000/compare
        def compare():
            user0, user1 = sorted(
                [requested.values['user1'], request.values['user2']])

            if user0 == user1:
                message = "cannot compare users to themselves!"

            else:
                prediction = predict_user(
                    user0, user1, request.values['tweet_text'])

                message = '{} is morelikely to have been said by {} than {}'.format(
                    request.values["tweet_text"], user1 if prediction else user0,
                    user0 if prediction else user1
                )

            return render_template('prediction.html', 
                                    title = "Prediction", 
                                    message = message)

        @app.route('/user', methods=["POST"]) # http://127.0.0.1:5000/user
    
    
        @app_route('/user/<name>', methods=["GET"]) # http://127.0.0.1:5000/user/<name>
        def user(name=None, message=''):
            name = name or request.values["user_name"]

            try:
                if request.method == "POST":
                    add_or_update_user(name)
                    message = "User {} was succesfully added!".format(name)

                tweets = User.query.filter(User.name == name).one().tweets

            except Execption as e:
                message = "Error adding {}: {}".format(name, e)
                tweets = []

            return render_template("user.html", 
                                    title=name, 
                                    tweets=tweets, 
                                    message = message)

    
    @app.route('/update')  # http://127.0.0.1:5000/update
    def update():
        insert_example_users()
        return render_template('base.html', title="Home", users=User.query.all())

    @app.route('/reset')  # http://127.0.0.1:5000/reset
    def reset():
        # we must create the database
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title="Home", users=User.query.all())


    return app

    

