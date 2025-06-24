from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse, FileResponse
from pathlib import Path
from src.config import YAML_OUTPUT_DIR
from src.scheme.service.request import ServiceCreateRequest
from src.generator.service_yaml import create_service_yaml


router = APIRouter()


@router.post("/yaml", response_class=PlainTextResponse)
def generate_service_yaml(req: ServiceCreateRequest):
    """
    서비스 배포용 YAML 생성 (예: Jupyter, VSCode 등)
    """
    return create_service_yaml(
        service_name=req.service_name,
        service_type=req.service_type,
        cluster_name=req.cluster_name
    )


@router.post("/yaml/save")
def save_service_yaml(req: ServiceCreateRequest):
    yaml_str = create_service_yaml(
        service_name=req.service_name,
        service_type=req.service_type,
        cluster_name=req.cluster_name
    )
    file_path = Path(YAML_OUTPUT_DIR) / f"{req.service_name}.yaml"
    file_path.write_text(yaml_str, encoding="utf-8")
    return JSONResponse(content={"message": "YAML saved", "path": str(file_path)})

@router.get("/yaml/download/{service_name}", response_class=FileResponse)
def download_service_yaml(service_name: str):
    file_path = Path(YAML_OUTPUT_DIR) / f"{service_name}.yaml"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="YAML file not found")
    return FileResponse(path=file_path, filename=file_path.name, media_type="application/x-yaml")
