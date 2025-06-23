from pathlib import Path

def get_yaml_file_path(file_name: str, output_dir: str) -> Path:
    """
    주어진 파일 이름에 대한 YAML 전체 경로 반환
    """
    return Path(output_dir) / f"{file_name}.yaml"


def yaml_file_exists(file_name: str, output_dir: str) -> bool:
    """
    해당 이름의 YAML 파일 존재 여부 확인
    """
    return get_yaml_file_path(file_name, output_dir).exists()
