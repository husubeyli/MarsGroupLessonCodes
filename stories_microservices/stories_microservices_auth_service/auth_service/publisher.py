import json

from auth_service.config.base import RedisConfig


class Publish(RedisConfig):

    def __init__(self, data, event_type):
        self.data = data
        self.event_type = event_type
        self.publish_data()

    @property
    def dump_data(self):
        message = {'data': self.data, 'event_type': self.event_type}
        return json.dumps(message)

    def publish_data(self):
        print(self.dump_data)
        self.client().publish(self.CHANNEL_NAME, self.dump_data)



