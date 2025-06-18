from fastapi import FastAPI
from src.router import get_all_routers

# FastAPI 애플리케이션 생성
def create_app() -> FastAPI:
    app = FastAPI(
        title="Ray Control Platform",
        description="Ray 클러스터 및 Serve, Job 등을 제어하는 REST API 플랫폼",
        version="1.0.0"
    )
    # 기능별 API 라우터 등록
    app.include_router(get_all_routers())
    return app
