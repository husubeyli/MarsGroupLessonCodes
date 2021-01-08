from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from routers import *

if __name__ == '__main__':
    app.run(port=5002, debug=True)
