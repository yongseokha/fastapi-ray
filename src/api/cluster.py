from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse, FileResponse
from pathlib import Path

from src.scheme.cluster.request import ClusterCreateRequest, ClusterDeleteRequest
from src.generator.cluster_yaml import (
    build_cluster_yaml,
    build_cluster_delete_yaml,
    save_cluster_yaml_to_file,
    save_cluster_delete_yaml_to_file,
)
from src.config import YAML_OUTPUT_DIR
import httpx

router = APIRouter()


@router.post("/yaml", response_class=PlainTextResponse)
async def generate_cluster_yaml(req: ClusterCreateRequest):
    """
    클러스터 생성 YAML 문자열 생성
    """
    return build_cluster_yaml(req)


@router.post("/yaml/save")
async def save_cluster_yaml(req: ClusterCreateRequest):
    """
    클러스터 생성 YAML 파일 저장
    """
    file_path = save_cluster_yaml_to_file(req)
    return JSONResponse(content={"message": "YAML saved successfully", "path": file_path})


@router.get("/yaml/download/{cluster_name}", response_class=FileResponse)
async def download_cluster_yaml(cluster_name: str):
    """
    저장된 클러스터 생성 YAML 파일 다운로드
    """
    file_path = Path(YAML_OUTPUT_DIR) / f"{cluster_name}.yaml"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="YAML file not found")
    return FileResponse(path=file_path, filename=f"{cluster_name}.yaml", media_type="application/x-yaml")


@router.post("/yaml/delete", response_class=PlainTextResponse)
async def generate_delete_yaml(req: ClusterDeleteRequest):
    """
    클러스터 삭제용 YAML 문자열 생성
    """
    return build_cluster_delete_yaml(req)


@router.post("/yaml/delete/save")
async def save_delete_yaml(req: ClusterDeleteRequest):
    """
    클러스터 삭제용 YAML 파일 저장
    """
    file_path = save_cluster_delete_yaml_to_file(req)
    return JSONResponse(content={"message": "Delete YAML saved successfully", "path": file_path})


@router.get("/yaml/delete/download/{cluster_name}", response_class=FileResponse)
async def download_delete_yaml(cluster_name: str):
    """
    저장된 클러스터 삭제 YAML 파일 다운로드
    """
    file_path = Path(YAML_OUTPUT_DIR) / f"{cluster_name}-delete.yaml"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="YAML file not found")
    return FileResponse(path=file_path, filename=f"{cluster_name}-delete.yaml", media_type="application/x-yaml")


@router.get("/status/{cluster_name}")
async def get_cluster_status(cluster_name: str):
    """
    Ray 클러스터 상태 조회
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://127.0.0.1:8265/api/cluster_summary")
            response.raise_for_status()
            cluster_info = response.json()

        # 여기서는 간단히 요약만 반환
        return JSONResponse(content={"cluster_name": cluster_name, "summary": cluster_info})
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ray Dashboard: {str(e)}")