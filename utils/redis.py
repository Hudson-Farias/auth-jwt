from redis import Redis
from json import dumps, loads

from dotenv import load_dotenv
from os import getenv

load_dotenv()

HOST = getenv('REDIS_HOST')
PASSWORD = getenv('REDIS_PASSWORD')
PORT = getenv('REDIS_PORT')

cache = Redis(host = HOST, port = PORT, password = PASSWORD, db = 0, decode_responses = True)

def set_cache(key, value, expiration_time: int = 60):
    data = dumps(value)
    cache.setex(key, expiration_time, data)


def get_cache(key):
    value = cache.get(key)
    if value: return loads(value)
