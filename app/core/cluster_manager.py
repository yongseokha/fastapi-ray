import subprocess
import time
import ray
import traceback

# def start_cluster():
#     try:
#         subprocess.run(["ray", "stop"], capture_output=True)
#
#         result = subprocess.run([
#             "ray", "start", "--head",
#             "--port=6379",
#             "--dashboard-port=8265",
#             "--include-dashboard=true",
#             "--num-cpus=2"
#         ], check=True, capture_output=True, text=True)
#
#         time.sleep(2)
#         return {"status": "success", "message": result.stdout}
#     except subprocess.CalledProcessError as e:
#         return {"status": "error", "message": e.stderr}

def start_cluster():
    try:
        subprocess.run(["ray", "stop"], capture_output=True)

        result = subprocess.run([
            "ray", "start", "--head",
            "--port=6379",
            #"--dashboard-port=false",
            "--include-dashboard=false",
            "--num-cpus=2",
            "--node-manager-port=30001",
            "--object-manager-port=30002",
            "--gcs-server-port=30003",
            "--metrics-export-port=30004",
            "--dashboard-agent-listen-port=30005",
            "--min-worker-port=30010",
            "--max-worker-port=30020"
        ], check=True, capture_output=True, text=True)

        time.sleep(2)
        return {"status": "success", "message": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr}


def stop_cluster():
    try:
        result = subprocess.run(
            ["ray", "stop"],
            check=True,
            capture_output=True,
            text=True
        )
        return {"status": "stopped", "message": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr}

import requests

# def get_status():
#     try:
#         dashboard_url = "http://127.0.0.1:8265/api/cluster_status"
#         response = requests.get(dashboard_url)
#         response.raise_for_status()
#
#         return {
#             "status": "running",
#             "data": response.json()
#         }
#
#     except Exception as e:
#         import traceback
#         return {
#             "status": "error",
#             "message": traceback.format_exc()
#         }

def get_status():
    try:
        ray.init(address="127.0.0.1:6379", ignore_reinit_error=True)

        nodes = ray.nodes()
        status = [
            {
                "NodeID": node["NodeID"],
                "Alive": node["Alive"],
                "Resources": node.get("Resources", {})
            }
            for node in nodes
        ]
        return {"status": "running", "nodes": status}
    except Exception as e:
        return {"status": "error", "message": traceback.format_exc()}
    finally:
        ray.shutdown()


