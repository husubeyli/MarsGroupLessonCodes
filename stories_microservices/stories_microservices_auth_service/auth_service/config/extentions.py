from datetime import timedelta

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from auth_service.app import app
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from flask_login import LoginManager
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db_user:bTmNECmEZOrdUcX4DQkAGevLtRakY@127.0.0.1:5433/db_name'
app.config['SECRET_KEY'] = 'this is private'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
jwt = JWTManager(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
swagger = Swagger(app)

