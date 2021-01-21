import redis
import json

from core.config import RedisConfig

from core.mail import SendMail


class Handler:

    def __init__(self, message):
        if message.get("type") == "message":
            self.data = self.serialize_data(message)
            if self.find_event_type():
                print('event type tapildi')
                mail_data = self.get_mail_data()
                self.send_mail(mail_data)
            else:
                print('event type tapilmadi')

    def find_event_type(self):
        event_type = self.data.get('event_type')
        if event_type and event_type == 'send_mail':
            return True
        return False

    def serialize_data(self, message):
        data = message.get('data')
        return json.loads(data)

    def get_mail_data(self):
        return self.data.get('data')

    def send_mail(self, mail_data):
        SendMail(**mail_data)


def subscribe():
    redis_conn = RedisConfig.client()
    p = redis_conn.pubsub()
    p.subscribe(**{RedisConfig.CHANNEL_NAME: Handler})
    thread = p.run_in_thread()
