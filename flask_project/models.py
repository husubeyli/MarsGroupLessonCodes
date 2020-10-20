from extensions import db, Model, Column, Integer, String, ForeignKey, relationship

class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    full_name = Column(String(80), nullable=False)
    phone_numbers = relationship('PhoneNumber', backref='user', lazy=True)

    def __repr__(self):
        return f"Username: {self.username} Email: {self.email} Full name: {self.full_name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, username, email, full_name):
        self.username = username
        self.email = email
        self.full_name = full_name

# PEP8
class PhoneNumber(Model):
    """
    This table keep user phone numbers
    """
    id = Column(Integer, primary_key=True)
    number = Column(String(15), nullable=False)
    person_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
