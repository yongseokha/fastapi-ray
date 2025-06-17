from fastapi import APIRouter
from app.core.cluster_manager import start_cluster, stop_cluster, get_status

router = APIRouter()

@router.post("/cluster/start")
def start():
    return start_cluster()

@router.post("/cluster/stop")
def stop():
    return stop_cluster()

@router.get("/cluster/status")
def status():
    return get_status()
