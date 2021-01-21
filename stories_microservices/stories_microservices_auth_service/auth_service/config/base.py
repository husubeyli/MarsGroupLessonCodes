import os
import redis


BASE_DIRS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIRS, 'media')


class RedisConfig:
    HOST = os.environ.get('HOST', 'localhost')
    PORT = os.environ.get('PORT', 6379)
    CHANNEL_NAME = 'events'
    PASSWORD = os.environ.get('PASSWORD', '12345')

    @classmethod
    def client(cls):
        return redis.Redis(host=cls.HOST, port=cls.PORT, password=cls.PASSWORD, db=0)