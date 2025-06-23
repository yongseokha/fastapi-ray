from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse, FileResponse, JSONResponse
from pathlib import Path
from src.config import YAML_OUTPUT_DIR
from src.scheme.cluster.request import ClusterCreateRequest
from src.generator.cluster_yaml import build_cluster_yaml, save_cluster_yaml_to_file

router = APIRouter()


@router.post("/yaml", response_class=PlainTextResponse)
async def generate_cluster_yaml(req: ClusterCreateRequest):
    """
    클러스터 YAML 문자열 생성
    """
    return build_cluster_yaml(req)


@router.post("/yaml/save")
async def save_cluster_yaml(req: ClusterCreateRequest):
    """
    클러스터 YAML 저장 후 경로 반환
    """
    file_path = save_cluster_yaml_to_file(req)
    return JSONResponse(content={"message": "YAML saved successfully", "path": file_path})


@router.get("/yaml/download/{cluster_name}", response_class=FileResponse)
async def download_cluster_yaml(cluster_name: str):
    """
    저장된 클러스터 YAML 다운로드
    """
    path = Path(YAML_OUTPUT_DIR) / f"{cluster_name}.yaml"
    if not path.exists():
        raise HTTPException(status_code=404, detail="YAML file not found")
    return FileResponse(path=path, filename=path.name, media_type="application/x-yaml")
