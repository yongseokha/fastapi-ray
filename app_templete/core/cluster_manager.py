import subprocess

def start_cluster():
    subprocess.run(["ray", "start", "--head", "--port=6379"])
    return {"status": "started"}

def stop_cluster():
    subprocess.run(["ray", "stop"])
    return {"status": "stopped"}

def get_status():
    import ray
    ray.init(address="auto")
    nodes = ray.nodes()
    return {"nodes": nodes}
