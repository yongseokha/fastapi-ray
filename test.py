import os

# 현재 디렉토리 기준
current_dir = os.getcwd()

# venv 디렉토리는 제외하고 .py 파일만 출력
for root, dirs, files in os.walk(current_dir):
    # venv 디렉토리 제외
    dirs[:] = [d for d in dirs if d != 'venv']

    # .py 파일만 필터링
    for file in files:
        if file.endswith('.py'):
            # 상대 경로로 출력
            rel_path = os.path.relpath(os.path.join(root, file), current_dir)
            print(rel_path)