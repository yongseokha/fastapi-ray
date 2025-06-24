from fastapi import FastAPI
from src.api import cluster, job, serve, service
from src.users import router as user_router
from src.services.router import router as service_router

def include_routers(app: FastAPI):
    """
    전체 API 라우터 통합
    """
    app.include_router(cluster.router, prefix="/cluster", tags=["Cluster"])
    app.include_router(serve.router, prefix="/serve", tags=["Serve"])
    app.include_router(job.router, prefix="/job", tags=["Job"])
    app.include_router(user_router.router, prefix="/user", tags=["User"])
    app.include_router(service.router, prefix="/service", tags=["Service"])

