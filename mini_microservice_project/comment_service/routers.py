import random
from app import app
from flask import jsonify, request


post_comment_list = [
    {
        'id': 1,
        'comments': [
            {
                'id': 1,
                'content': 'sdjknf'
            }
        ]
    },
    {
        'id': 2,
        'comments': [
            {
                'id': 1,
                'content': 'sdjknf'
            }
        ]
    },
]


@app.route('/posts/<int:id>/comments/', methods=['GET', 'POST'])
def comments(id):
    if request.method == 'POST':
        new_comment_data = request.json or request.form
        new_comment_data = dict(new_comment_data)
        for post in post_comment_list:
            if post['id'] == id:
                post.setdefault("comments", [])
                new_comment_data.update({
                    'id': random.randint(1, 10000)
                })
                post['comments'].append(new_comment_data)
                return jsonify(post)
        return jsonify({'detail': 'Not found'}), 404
    found_post = list(filter(lambda post: post['id'] == id, post_comment_list))
    if not found_post:
        return jsonify({'detail': 'Not found'}), 404
    return jsonify(found_post[0])


@app.route('/events/', methods=['POST'])
def events():
    event_data = dict(request.json)
    event_type = event_data.get('event_type')
    if event_type and event_type == 'PostCreated':
        post_data = event_data.get('data')
        post_comment_list.append(post_data)
    return jsonify(post_comment_list)




