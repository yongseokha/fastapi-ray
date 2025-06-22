from fastapi import FastAPI
from src.router import include_routers

def create_app() -> FastAPI:
    """
    FastAPI 앱 객체 생성 및 라우터 등록
    """
    app = FastAPI(title="Ray Control Platform", version="0.1.0")
    include_routers(app)
    return app
