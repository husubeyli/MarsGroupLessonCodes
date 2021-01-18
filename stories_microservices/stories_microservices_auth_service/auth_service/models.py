from auth_service.config.extentions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates
from flask_login import UserMixin
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(254), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    date_joined = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    bio = db.Column(db.TEXT, nullable=True)
    image = db.Column(db.String(500), nullable=True)
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, username, password, first_name=None, last_name=None, bio=None,
                 image=None, is_active=False, is_superuser=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.is_active = is_active
        self.bio = bio
        self.image = image
        self.is_superuser = is_superuser

    def save(self):
        db.session.add(self)
        db.session.commit()
