import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# get the environment variable from the .env file
salainen_avain = os.getenv("salainen-avain")
print(salainen_avain)