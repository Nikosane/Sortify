import json
import os
import shutil

def undo_operations():
    log_file = "file_operations.json"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            operations = json.load(f)
        for operation in reversed(operations):
            shutil.move(operation["dst"], operation["src"])
        os.remove(log_file)
        print("Undo completed successfully.")
    else:
        print("No operations to undo.")

if __name__ == "__main__":
    undo_operations()
