import random
from app import app
from flask import jsonify, request

from publisher import send

post_list = [
    {
        'id': 1,
        'title': 'New Post'
    },
    {
        'id': 2,
        'title': 'New Post 2'
    },
]


@app.route('/posts/', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        new_post_data = dict(request.json or request.form)
        print(new_post_data)
        new_post_data.update({
            'id': random.randint(1, 1000)
        })
        post_list.append(new_post_data)
        send(new_post_data)
        return jsonify(new_post_data), 201
    return jsonify(post_list)


@app.route('/events/', methods=['POST'])
def events():
    event_data = dict(request.json)
    event_type = event_data.get('event_type')

    return jsonify({})



