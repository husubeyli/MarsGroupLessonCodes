import random
from app import app
from flask import jsonify, request


post_comment_list = [
    {
        'id': 1,
        'title': 'New Post',
        'comments': [
            {
                'id': 1,
                'content': 'sdjknf'
            }
        ]
    },
    {
        'id': 2,
        'title': 'New Post 2',
        'comments': [
            {
                'id': 1,
                'content': 'sdjknf'
            }
        ]
    },
]


@app.route('/posts/')
def posts():
    return jsonify(post_comment_list)


@app.route('/events/', methods=['POST'])
def events():
    event_data = dict(request.json)
    event_type = event_data.get('event_type')
    if event_type and event_type == 'PostCreated':
        post_data = event_data.get('data')
        post_comment_list.append(post_data)
    return jsonify(post_comment_list)




