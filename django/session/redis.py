import redis, environ

# Read .env file.
env = environ.Env()
env.read_env('.env')

COMPANY_ID_PREFIX = "company_id"

class SessionRedis():
    def __init__(self):
        self.redis = redis.Redis(env('REDIS_HOST'), port = 6379)

    def get(self, token):
        timestamp = self.redis.get(token)
        company_id = self.redis.get(token + COMPANY_ID_PREFIX)
        return timestamp, company_id

    def setToken(self, token, time, company_id):
        self.redis.set(token, time)
        self.redis.set(token + COMPANY_ID_PREFIX, company_id)
        return

    def delete(self, token):
        self.redis.delete(token, token + COMPANY_ID_PREFIX)
        return
