from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse, FileResponse
from src.scheme.serve.request import ServeAppCreateRequest
from src.generator.serve_yaml import build_serve_yaml, save_serve_yaml_to_file
from src.config import YAML_OUTPUT_DIR
from pathlib import Path

router = APIRouter()


@router.post("/yaml", response_class=PlainTextResponse)
async def generate_serve_yaml(req: ServeAppCreateRequest):
    """
    Serve YAML 문자열을 생성해서 반환
    """
    return build_serve_yaml(req)


@router.post("/yaml/save")
async def save_serve_yaml(req: ServeAppCreateRequest):
    """
    Serve YAML 파일을 저장 후 경로 반환
    """
    file_path = save_serve_yaml_to_file(req)
    return JSONResponse(content={"message": "YAML saved successfully", "path": file_path})


@router.get("/yaml/download/{app_name}", response_class=FileResponse)
async def download_serve_yaml(app_name: str):
    """
    저장된 Serve YAML 파일을 다운로드
    """
    file_path = Path(YAML_OUTPUT_DIR) / f"{app_name}.yaml"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="YAML file not found")
    return FileResponse(path=file_path, filename=f"{app_name}.yaml", media_type="application/x-yaml")