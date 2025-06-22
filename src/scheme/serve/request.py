from pydantic import BaseModel, Field
from typing import List

class DeploymentSpec(BaseModel):
    name: str = Field(..., example="model-deploy")
    num_replicas: int = Field(1, example=2)

class ServeAppCreateRequest(BaseModel):
    app_name: str = Field(..., example="my-serve-app")
    import_path: str = Field(..., example="my_app.entrypoint:app")
    route_prefix: str = Field(..., example="/myapp")
    deployments: List[DeploymentSpec]
