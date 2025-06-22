from typing import List, Optional
from pydantic import BaseModel, Field


class RayJobCreateRequest(BaseModel):
    """
    Ray Job YAML 생성을 위한 요청 스키마
    """
    job_name: str = Field(..., example="train-job")
    entrypoint: str = Field(..., example="python train.py")
    cluster_name: str = Field(..., example="ray-cluster-01")
    working_dir: Optional[str] = Field(None, example="https://github.com/user/repo/archive/main.zip")
    pip_packages: Optional[List[str]] = Field(default_factory=list, example=["pandas", "scikit-learn"])
