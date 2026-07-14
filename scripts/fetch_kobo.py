import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API = os.getenv("KOBO_API")
TOKEN = os.getenv("KOBO_TOKEN")


def fetch_kobo():

    headers = {
        "Authorization": f"Token {TOKEN}"
    }

    response = requests.get(API, headers=headers)

    response.raise_for_status()

    data = response.json()["results"]

    return pd.json_normalize(data)
