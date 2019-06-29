## App Utilities
import os
# import env
from db import db

from flask import Flask, render_template
from flask_restful import Api
from flask_bootstrap import Bootstrap
from flask_s3 import FlaskS3

from resources.user import UserRegister, UserLogin, UserLogout, login_manager
from resources.algorithms import Environment, Pathfinder

## App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['FLASKS3_BUCKET_NAME'] = os.environ.get('FLASKS3_BUCKET_NAME')

app.config['DEBUG'] = False
api = Api(app)

Bootstrap(app)
login_manager.init_app(app)
s3 = FlaskS3(app)

## Register Resources
api.add_resource(Environment, '/environment')
api.add_resource(Pathfinder, '/pathfinder')

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')




## Main View
@app.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


# DB INIT
db.init_app(app)

# APP INITIATION
if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run()

# Docker
#     app.run(host='0.0.0.0')

# Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
