import psutil

def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=1)

def get_memory_usage() -> float:
    return psutil.virtual_memory().used / (1024 ** 3)  # GB
