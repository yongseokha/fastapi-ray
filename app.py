import uvicorn
from src.server import create_app

app = create_app()

# 개발용 실행 엔트리포인트
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
