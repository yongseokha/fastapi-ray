from fastapi import Depends, HTTPException, status
from src.users.utils import get_mock_user
from src.users.models import Role


def verify_permission(required_role: Role):
    def dependency(user: dict = Depends(get_mock_user)):
        if user["role"] != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="권한이 부족합니다."
            )
        return user
    return dependency


def get_current_user():
    """
    사용자 인증 훅 (Keycloak/JWT 연동 예정)
    """
    return {
        "username": "mock_user",
        "role": "user"
    }
