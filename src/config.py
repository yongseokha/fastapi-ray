import os

# 저장될 YAML 디렉토리
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
YAML_OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs", "job_yaml")

# 디렉토리가 없으면 생성
os.makedirs(YAML_OUTPUT_DIR, exist_ok=True)
