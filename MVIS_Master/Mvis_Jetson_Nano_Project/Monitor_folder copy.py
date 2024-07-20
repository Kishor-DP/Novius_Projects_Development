import os
import time

class FileRotator:
    def __init__(self, folder_path, file_limit=500):
        self.folder_path = folder_path
        self.file_limit = file_limit

    def get_file_list(self):
        files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path)]
        files = [f for f in files if os.path.isfile(f)]
        return files

    def delete_oldest_file(self, files):
        oldest_file = min(files, key=os.path.getctime)
        os.remove(oldest_file)
        print(f"Deleted {oldest_file}")

    def monitor_folder(self):
        while True:
            files = self.get_file_list()
            if len(files) > self.file_limit:
                self.delete_oldest_file(files)
            time.sleep(1)  # Check every second

if __name__ == "__main__":
    folder_path = "images/Track"  # Change this to your folder path
    file_rotator = FileRotator(folder_path)
    file_rotator.monitor_folder()
