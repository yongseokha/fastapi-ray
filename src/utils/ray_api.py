# src/core/ray_api.py

import requests
from src.config import settings
from fastapi import HTTPException

def ray_get(path: str):
    """
    Ray Dashboard로 GET 요청을 보냅니다.
    예: /api/serve/applications/
    """
    url = f"{settings.RAY_DASHBOARD_URL}{path}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ray GET 요청 실패: {str(e)}")


def ray_post(path: str, data: dict):
    """
    Ray Dashboard로 POST 요청을 보냅니다.
    예: /api/jobs/
    """
    url = f"{settings.RAY_DASHBOARD_URL}{path}"
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ray POST 요청 실패: {str(e)}")


def ray_delete(path: str):
    """
    Ray Dashboard로 DELETE 요청을 보냅니다.
    예: /api/serve/applications/{app_name}
    """
    url = f"{settings.RAY_DASHBOARD_URL}{path}"
    try:
        response = requests.delete(url)
        response.raise_for_status()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ray DELETE 요청 실패: {str(e)}")
