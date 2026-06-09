from src.process_scanner import get_running_processes
from src.startup_checker import get_startup_entries
from src.detector import analyze_processes
from src.report_generator import save_report

def main():

    print("Scanning processes...")

    processes = get_running_processes()

    findings = analyze_processes(processes)

    print("Checking startup entries...")

    startup_entries = get_startup_entries()

    report = save_report(
        findings,
        startup_entries
    )

    print(f"Report saved: {report}")

if __name__ == "__main__":
    main()