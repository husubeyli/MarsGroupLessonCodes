import redis
import json


redis_conn = redis.Redis(host='localhost', port=6379, password='12345', db=0)


def handler(message):
    if message.get("type") == "message":
        json_data = message.get("data")
        data = json.loads(json_data)
        a = data['a']
        b = data['b']
        operation = data['operation']
        if operation == 'sum':
            print('a+b', a+b)
        elif operation == 'sum':
            print('a+b=', a+b)

p = redis_conn.pubsub()
p.subscribe(**{'broadcast': handler})
thread = p.run_in_thread()

# pubsub = redis_conn.pubsub()
# pubsub.subscribe("broadcast")
# for message in pubsub.listen():
#     if message.get("type") == "message":
#         json_data = message.get("data")
#         data = json.loads(json_data)
#         a = data['a']
#         b = data['b']
#         operation = data['operation']
#         if operation == 'sum':
#             print('a+b', a+b)
#         elif operation == 'sum':
#             print('a+b=', a+b)


