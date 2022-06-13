from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)

# r = redis.Redis()
redis_url = os.getenv('REDIS_URL')

r = redis.from_url(redis_url)

q = Queue(connection=r)

from queue_app import views
from queue_app import tasks
