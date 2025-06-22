from pydantic import BaseModel, Field
from typing import Literal


class ClusterCreateRequest(BaseModel):
    """
    클러스터 생성 요청에 사용되는 스키마 정의
    """
    cluster_name: str = Field(..., example="ray-cluster-01", description="클러스터 이름")
    cluster_type: Literal["public", "private"] = Field(..., example="private", description="클러스터 유형")
    num_cpus: int = Field(1, ge=1, description="Head 노드 CPU 수")
    num_workers: int = Field(1, ge=0, description="Worker 노드 수")

class ClusterDeleteRequest(BaseModel):
    cluster_name: str = Field(..., example="ray-test")

