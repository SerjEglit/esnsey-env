import time
import random

def monitor_metrics():
    while True:
        print(f"[{time.ctime()}] CPU: {random.randint(10,50)}% | MEM: {random.randint(1,8)}GB")
        time.sleep(2)

if __name__ == "__main__":
    monitor_metrics()
