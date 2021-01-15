from flask import Flask


app = Flask(__name__)

from auth_service.config.extentions import db
from auth_service.models import *
from auth_service.api.routers import *

# app.config["APPLICATION_ROOT"] = "api/v1.0/post/"

if __name__ == '__main__':
    # app.init_app(db)
    app.run(port=5001, debug=True)

