import os
from dotenv import load_dotenv

load_dotenv()  # If using a .env file

SECRET_KEY = os.getenv("SECRET_KEY")

if SECRET_KEY:
    print("SECRET_KEY loaded successfully!")
else:
    print("SECRET_KEY is missing!")