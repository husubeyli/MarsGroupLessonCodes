import redis
import json

redis_conn = redis.Redis(host='localhost', port=6379, password='12345', db=0)
a = int(input('A daxil edin:'))
b = int(input('b daxil edin:'))
d = {
    'a': a,
    'b': b,
    'operation': "sum"
}
redis_conn.publish("broadcast", json.dumps(d))

