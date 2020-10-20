from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/project'
from extensions import db, migrate
from models import *
from controllers import *


if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)
    app.run(debug=True, port=5000)
