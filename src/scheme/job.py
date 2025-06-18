# src/scheme/job.py

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict
from typing import Optional, Dict

class JobSubmitRequest(BaseModel):
    """
    Ray Job을 제출할 때 사용하는 요청 스키마입니다.
    """
    entrypoint: str = Field(..., description="실행할 Python 명령 또는 파일 경로")
    runtime_env: Optional[Dict] = Field(
        default_factory=dict,
        description="필요한 패키지, 환경 설정 등이 포함된 런타임 환경"
    )
    job_id: Optional[str] = Field(
        default=None,
        description="옵션: 특정 Job ID를 지정 (미지정 시 자동 생성)"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "entrypoint": "python script.py",
                "runtime_env": {
                    "working_dir": "https://github.com/example/repo.zip",
                    "pip": ["pandas", "requests"]
                },
                "job_id": "my-custom-job-id"
            }
        }
    )