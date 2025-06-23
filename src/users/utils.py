from src.users.models import Role

def get_mock_user():
    """
    인증 시스템 연동 전까지 사용할 임시 사용자
    """
    return {
        "username": "test-user",
        "role": Role.USER  # 또는 Role.SYSTEM
    }
