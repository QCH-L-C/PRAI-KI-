import os

LOG_DIRECTORY = "/home/runner/logs"
DEBUG_OUTPUT_FILE = "/home/runner/debug_output.log"

def collect_logs():
    """Sammelt und speichert Runner-Logs."""
    try:
        with open(DEBUG_OUTPUT_FILE, "w") as output_file:
            for root, dirs, files in os.walk(LOG_DIRECTORY):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as log_file:
                        output_file.write(f"==== Inhalt von {file_path} ====\n")
                        output_file.write(log_file.read())
                        output_file.write("\n\n")
        print(f"Logs wurden in {DEBUG_OUTPUT_FILE} gespeichert.")
    except Exception as e:
        print(f"Fehler beim Sammeln der Logs: {e}")

if __name__ == "__main__":
    collect_logs()
