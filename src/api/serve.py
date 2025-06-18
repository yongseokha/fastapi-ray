from fastapi import APIRouter
from src.scheme.serve import ServeDeployRequest
from src.utils.ray_api import ray_post, ray_delete, ray_get

router = APIRouter(prefix="/serve", tags=["Serve"])

@router.post("/deploy")
def deploy_serve(request: ServeDeployRequest):
    """
    [Serve 앱 배포 API]
    - Serve 애플리케이션 사양(JSON)을 Ray Serve API에 전달하여 배포
    """
    return ray_post("/api/serve/applications/", request.dict()).json()

@router.get("/apps")
def list_apps():
    """
    [Serve 앱 목록 조회 API]
    - 현재 클러스터에 배포된 Serve 애플리케이션 목록을 반환
    """
    return ray_get("/api/serve/applications/").json()

@router.delete("/delete/{app_name}")
def delete_app(app_name: str):
    """
    [Serve 앱 삭제 API]
    - Serve에 배포된 앱을 이름 기준으로 삭제
    """
    return ray_delete(f"/api/serve/applications/{app_name}").json()
