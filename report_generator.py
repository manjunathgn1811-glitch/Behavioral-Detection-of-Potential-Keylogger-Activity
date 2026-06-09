from datetime import datetime

def save_report(findings, startup_entries):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"reports/report_{timestamp}.txt"

    with open(filename, "w") as f:

        f.write("=== Behavioral Detection Report ===\n\n")

        f.write("Suspicious Findings\n")
        f.write("-------------------\n")

        if findings:
            for item in findings:
                f.write(item + "\n")
        else:
            f.write("No suspicious findings.\n")

        f.write("\nStartup Entries\n")
        f.write("-------------------\n")

        for entry in startup_entries:
            f.write(entry + "\n")

    return filename