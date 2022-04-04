from environs import Env

env = Env()
env.read_env()

# postgres connection
DATABASE_URL = env.str("DATABASE_URL")
SERVER_HOST = env.str("SERVER_HOST")
SERVER_PORT = env.int("SERVER_PORT")

# s3 connection
ENDPOINT_URL = env.str("ENDPOINT_URL")
BUCKET = env.str("BUCKET")
ACCESS_KEY = env.str("ACCESS_KEY")
SECRET_KEY = env.str("SECRET_KEY")
