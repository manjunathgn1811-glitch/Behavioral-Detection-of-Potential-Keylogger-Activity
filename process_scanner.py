import psutil

def get_running_processes():
    processes = []

    for proc in psutil.process_iter(
        ['pid', 'name', 'exe', 'cpu_percent']
    ):
        try:
            processes.append(proc.info)
        except Exception:
            pass

    return processes