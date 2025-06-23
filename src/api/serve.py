from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse, FileResponse
from src.scheme.serve.request import ServeAppCreateRequest
from src.generator.serve_yaml import (
    build_serve_yaml, save_serve_yaml_to_file,
    build_serve_delete_yaml, save_serve_delete_yaml_to_file
)
from src.config import YAML_OUTPUT_DIR
from pathlib import Path
import httpx



router = APIRouter()


@router.post("/yaml", response_class=PlainTextResponse)
async def generate_serve_yaml(req: ServeAppCreateRequest):
    return build_serve_yaml(req)


@router.post("/yaml/save")
async def save_serve_yaml(req: ServeAppCreateRequest):
    file_path = save_serve_yaml_to_file(req)
    return JSONResponse(content={"message": "YAML saved successfully", "path": file_path})


@router.get("/yaml/download/{app_name}", response_class=FileResponse)
async def download_serve_yaml(app_name: str):
    file_path = Path(YAML_OUTPUT_DIR) / f"{app_name}.yaml"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="YAML file not found")
    return FileResponse(path=file_path, filename=f"{app_name}.yaml", media_type="application/x-yaml")


@router.get("/yaml/delete/{app_name}", response_class=PlainTextResponse)
async def generate_serve_delete_yaml(app_name: str):
    return build_serve_delete_yaml(app_name)


@router.get("/yaml/delete/save/{app_name}")
async def save_serve_delete_yaml(app_name: str):
    file_path = save_serve_delete_yaml_to_file(app_name)
    return JSONResponse(content={"message": "Delete YAML saved", "path": file_path})


@router.get("/apps")
async def list_serve_apps():
    """
    Serve 앱 목록을 Mock 형태로 반환
    """
    apps = [
        {
            "app_name": "image-classifier",
            "status": "RUNNING",
            "route_prefix": "/image",
            "deployments": [
                {"name": "resnet", "replicas": 2},
                {"name": "preprocessor", "replicas": 1}
            ]
        },
        {
            "app_name": "text-generator",
            "status": "STOPPED",
            "route_prefix": "/text",
            "deployments": [
                {"name": "gpt2", "replicas": 1}
            ]
        }
    ]
    return {"apps": apps}


@router.get("/status/{app_name}")
async def get_serve_status(app_name: str):
    """
    Ray Serve 앱 상태 조회
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://127.0.0.1:8265/api/serve/applications")
            response.raise_for_status()
            apps = response.json().get("applications", [])

        matched_app = next((app for app in apps if app["name"] == app_name), None)
        if not matched_app:
            raise HTTPException(status_code=404, detail="Serve app not found")

        return JSONResponse(content=matched_app)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ray Serve API: {str(e)}")

