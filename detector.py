SUSPICIOUS_KEYWORDS = [
    "logger",
    "hook",
    "monitor",
    "capture",
    "record"
]

def analyze_processes(processes):
    findings = []

    for proc in processes:
        name = str(proc.get("name", "")).lower()

        for keyword in SUSPICIOUS_KEYWORDS:
            if keyword in name:
                findings.append(
                    f"Potentially suspicious process: {proc['name']}"
                )

    return findings