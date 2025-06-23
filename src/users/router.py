from fastapi import APIRouter, Depends
from src.users.dependencies import verify_permission
from src.users.models import Role

router = APIRouter()

@router.get("/admin-only")
async def admin_only_route(user=Depends(verify_permission(Role.SYSTEM))):
    return {"message": f"{user['username']}은(는) 관리자입니다."}
