# src/scheme/cluster.py

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class ClusterDeployRequest(BaseModel):
    """
    Ray 클러스터를 배포할 때 필요한 자원 설정 요청 모델입니다.
    이 모델은 FastAPI의 요청 body로 사용됩니다.
    """
    num_cpus: int = Field(..., gt=0, description="사용할 CPU 개수")
    num_gpus: int = Field(default=0, ge=0, description="사용할 GPU 개수 (기본값 0)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "num_cpus": 2,
                "num_gpus": 1
            }
        }
    )