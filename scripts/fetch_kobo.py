import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

KOBO_API = os.getenv("KOBO_API")
KOBO_TOKEN = os.getenv("KOBO_TOKEN")


def fetch_kobo():
    headers = {
        "Authorization": f"Token {KOBO_TOKEN}"
    }

    response = requests.get(KOBO_API, headers=headers)
    response.raise_for_status()

    data = response.json()["results"]

    df = pd.json_normalize(data)

    return df