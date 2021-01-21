import os

import redis


class EmailConfig:
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'tech.academy.docker@gmail.com'
    EMAIL_HOST_PASSWORD = 'suqmnhaxezvemyhn'


class RedisConfig:
    HOST = os.environ.get('HOST', 'localhost')
    PORT = os.environ.get('PORT', 6379)
    CHANNEL_NAME = 'events'
    PASSWORD = os.environ.get('PASSWORD', '12345')

    @classmethod
    def client(cls):
        return redis.Redis(host=cls.HOST, port=cls.PORT, password=cls.PASSWORD, db=0)
