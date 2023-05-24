import os
import requests
from bardapi import Bard
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the token from the environment variable
token = os.environ.get("BARD_API_TOKEN")

# Set up the API access token and session
session = requests.Session()
session.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}
session.cookies.set("__Secure-1PSID", token)

# Create an instance of the Bard class
bard = Bard(token=token, session=session)

# Function to get answer from the Bard API
def get_bard_answer(question):
    # Query the Bard API for the answer
    answer = bard.get_answer(question)
    content = answer['content']
    return content
