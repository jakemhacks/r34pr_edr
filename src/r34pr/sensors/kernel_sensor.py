# Kernel process sensor

import psutil
import datetime


def get_cpu_percent() -> float:
    # Grab current CPU usage
    percent: float = psutil.cpu_percent(interval=1)
    return percent


def get_running_processes() -> dict:
    # create a dictionary of all current running processes
    procs = {p.pid: p.info for p in psutil.process_iter(["name", "username"])}
    return procs


def print_procs() -> None:
    # This is a current test function to make sure things are working so far
    for proc in psutil.process_iter(
        ["pid", "name", "username", "status", "create_time"]
    ):
        if proc.info["status"] == "running":
            print(
                f"{proc.info['name']}: Started: {datetime.datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')}"
            )
