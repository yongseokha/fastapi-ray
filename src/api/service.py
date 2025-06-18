from fastapi import APIRouter
from src.utils.ray_api import ray_get

router = APIRouter(prefix="/service", tags=["Service"])

@router.get("/list")
def list_services():
    """
    [Serve 앱의 서비스 목록 조회 API]
    - Serve 내부 라우팅된 서비스 목록 조회
    """
    return ray_get("/api/serve/applications/").json()
