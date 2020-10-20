from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from run import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

Model, Column, Integer, String, ForeignKey, relationship = db.Model, db.Column, db.Integer, db.String, db.ForeignKey, db.relationship

