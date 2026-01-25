# This is the main detection engine for the program

import psutil
import datetime


def get_cpu_percent() -> float:
    percent: float = psutil.cpu_percent(interval=1)
    return percent


def get_running_processes() -> dict:
    procs = {p.pid: p.info for p in psutil.process_iter(["name", "username"])}
    return procs


def print_procs() -> None:
    for proc in psutil.process_iter(
        ["pid", "name", "username", "status", "create_time"]
    ):
        if proc.info["status"] == "running":
            print(
                f"{proc.info['name']}: Started: {datetime.datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')}"
            )
