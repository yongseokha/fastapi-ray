from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Ray Dashboard API 서버 주소
    RAY_DASHBOARD_URL: str = "http://localhost:8265"

# 이 설정 인스턴스를 외부에서 import 가능하게 만들어줍니다
settings = Settings()