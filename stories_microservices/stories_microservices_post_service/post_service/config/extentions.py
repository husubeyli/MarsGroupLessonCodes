from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from post_service.app import app
from flask_marshmallow import Marshmallow
from flasgger import Swagger

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db_user:bTmNECmEZOrdUcX4DQkAGevLtRakY@127.0.0.1:5432/db_name'
app.config['SECRET_KEY'] = 'this is private'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
swagger = Swagger(app)