from pydantic import BaseModel, Field
from typing import Literal

class ServiceCreateRequest(BaseModel):
    service_name: str = Field(..., example="jupyter-service")
    service_type: Literal["jupyter", "vscode", "application"] = Field(..., example="jupyter")
    cluster_name: str = Field(..., example="ray-private-cluster")
