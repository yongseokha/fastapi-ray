from fastapi import APIRouter
from app.core.job_manager import submit_job
from app.core.serve_manager import deploy_model

router = APIRouter()

@router.post("/job/submit")
def run_job(payload: dict):
    return submit_job(payload)

@router.post("/serve/deploy")
def serve(payload: dict):
    return deploy_model(payload)
