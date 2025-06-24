from pydantic import BaseModel, Field
from typing import Literal


class ServiceCreateRequest(BaseModel):
    """
    사용자 환경(Jupyter, VSCode 등) 배포 요청
    """
    name: str = Field(..., example="jupyter-env")
    service_type: Literal["jupyter", "vscode", "app"] = Field(..., example="jupyter")
    cluster_name: str = Field(..., example="ray-cluster-01")
