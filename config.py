import os
import environs

try:
    env = environs.Env()
    env.read_env("./.env")
except FileNotFoundError:
    print("No .env file found, using os.environ.")

API_ID = int(os.getenv("API_ID", env.int("API_ID")))
API_HASH = os.getenv("API_HASH", env.str("API_HASH"))
SESSION_STRING = os.getenv("SESSION_STRING", env.str("SESSION_STRING"))
