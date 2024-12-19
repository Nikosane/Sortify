import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileOrganizerHandler(FileSystemEventHandler):
    def __init__(self, target_folder):
        self.target_folder = target_folder

    def on_modified(self, event):
        for filename in os.listdir(self.target_folder):
            file_path = os.path.join(self.target_folder, filename)
            if os.path.isfile(file_path):
                self.organize_file(file_path)

    def organize_file(self, file_path):
        file_type = file_path.split('.')[-1].lower()
        destination_folder = os.path.join(self.target_folder, file_type.capitalize() + "_Files")
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

def start_monitoring(folder_to_monitor):
    event_handler = FileOrganizerHandler(folder_to_monitor)
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=True)
    observer.start()
    print(f"Monitoring changes in {folder_to_monitor}...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_monitor = input("Enter the folder path to monitor: ")
    start_monitoring(folder_to_monitor)
