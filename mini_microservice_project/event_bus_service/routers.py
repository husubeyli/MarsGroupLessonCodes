import requests
from flask import jsonify, request
from app import app


@app.route('/events/', methods=['POST'])
def posts():
    new_data = dict(request.json or request.form)
    requests.post('http://localhost:5002/events/', json=new_data)
    requests.post('http://localhost:5001/events/', json=new_data)
    requests.post('http://localhost:5003/events/', json=new_data)
    return jsonify(new_data), 201
