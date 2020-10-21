from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, DataRequired, Email


class UserForm(FlaskForm):
    """
    User Form for validate user data
    """
    username = StringField("Istifadeci adi", [Length(min=2, max=80), DataRequired()])
    email = StringField("E poct:", [Length(min=5, max=20), DataRequired(), Email()])
    full_name = StringField("Ad Soyad", [Length(min=5, max=50), DataRequired()])
