from fastapi import APIRouter
from src.api import cluster, job, serve, service

# 모든 기능별 API를 하나의 router로 묶어서 반환
def get_all_routers() -> APIRouter:
    router = APIRouter()
    router.include_router(cluster.router)
    router.include_router(job.router)
    router.include_router(serve.router)
    router.include_router(service.router)
    return router
