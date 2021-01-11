from flask import Flask


app = Flask(__name__)

from post_service.config.extentions import db
from post_service.models import *
from post_service.api.routers import *

# app.config["APPLICATION_ROOT"] = "api/v1.0/post/"

if __name__ == '__main__':
    # app.init_app(db)
    app.run(port=5001, debug=True)

