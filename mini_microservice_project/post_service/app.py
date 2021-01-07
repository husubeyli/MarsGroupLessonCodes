from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

from routers import *

CORS(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
