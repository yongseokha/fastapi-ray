# src/scheme/serve.py

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict
from typing import Dict, Any

class ServeDeployRequest(BaseModel):
    """
    Ray Serve 애플리케이션을 배포할 때 사용하는 요청 스키마입니다.
    이 형식은 Ray Serve HTTP API에서 요구하는 사양과 일치해야 합니다.
    """
    name: str = Field(..., description="배포할 Serve 앱 이름")
    import_path: str = Field(..., description="서비스 엔드포인트의 Python 경로 (예: module.Graph)")
    route_prefix: str = Field(..., description="라우팅할 URL prefix (예: /chat)")
    runtime_env: Dict[str, Any] = Field(
        default_factory=dict,
        description="필요한 의존성 또는 working_dir 등"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "chatbot-service",
                "import_path": "app.chat:ChatService",
                "route_prefix": "/chat",
                "runtime_env": {
                    "working_dir": "s3://bucket/code.zip",
                    "pip": ["openai", "fastapi"]
                }
            }
        }
    )