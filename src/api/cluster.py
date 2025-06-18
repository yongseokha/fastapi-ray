from fastapi import APIRouter, Depends, Header, HTTPException
from src.scheme.cluster import ClusterDeployRequest
from src.users.dependencies import verify_permission
import subprocess

# 클러스터 관련 API 라우터 등록
router = APIRouter(prefix="/cluster", tags=["Cluster"])

@router.post("/deploy")
def deploy_cluster(
    request: ClusterDeployRequest,
    x_user: str = Header(...),
    authorized: bool = Depends(lambda: verify_permission("deploy_cluster"))
):
    """
    [권한 기반 클러스터 배포 API]
    - CPU/GPU 자원 설정 값을 받아서 Ray 클러스터를 실행
    - 권한이 없는 사용자는 403 에러 반환
    """
    command = [
        "ray", "start", "--head",
        f"--num-cpus={request.num_cpus}",
        f"--num-gpus={request.num_gpus}"
    ]
    subprocess.Popen(command)
    return {"message": f"Cluster deployed with CPU: {request.num_cpus}, GPU: {request.num_gpus}"}


@router.post("/stop")
def stop_cluster(x_user: str = Header(...)):
    """
    [클러스터 중지 API]
    - Ray 클러스터를 종료
    """
    subprocess.call(["ray", "stop"])
    return {"message": "Ray cluster stopped"}
