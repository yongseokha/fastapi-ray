from fastapi import APIRouter
from app.core import cluster_manager

router = APIRouter()

@router.post("/cluster/start", summary="Ray 클러스터 시작")
def start_cluster():
    return cluster_manager.start_cluster()

@router.post("/cluster/stop", summary="Ray 클러스터 정지")
def stop_cluster():
    return cluster_manager.stop_cluster()

@router.get("/cluster/status", summary="Ray 클러스터 상태 조회")
def cluster_status():
    return cluster_manager.get_status()
