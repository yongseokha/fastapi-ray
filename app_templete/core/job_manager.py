import requests
from app.config import RAY_HEAD_ADDRESS

def submit_job(payload: dict):
    response = requests.post(f"{RAY_HEAD_ADDRESS}/api/jobs/", json=payload)
    return response.json()
