import os

def get_startup_entries():
    startup_folder = os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
    )

    entries = []

    if os.path.exists(startup_folder):
        for item in os.listdir(startup_folder):
            entries.append(item)

    return entries