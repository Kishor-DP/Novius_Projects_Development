import os
import time
import shutil

class FileRotator:
    def __init__(self, folder_paths, file_limit=500, monitored_folder="/home/jetson/Documents/", folder_limit=10):
        self.folder_paths = folder_paths
        self.file_limit = file_limit
        self.monitored_folder = monitored_folder
        self.folder_limit = folder_limit

    def get_file_list(self, folder_path):
        files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
        files = [f for f in files if os.path.isfile(f)]
        return files

    def get_folder_list(self, folder_path):
        folders = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
        folders = [f for f in folders if os.path.isdir(f)]
        return folders

    def delete_oldest_file(self, files):
        oldest_file = min(files, key=os.path.getctime)
        os.remove(oldest_file)
        print(f"Deleted {oldest_file}")

    def delete_oldest_folder(self, folders):
        oldest_folder = min(folders, key=os.path.getctime)
        shutil.rmtree(oldest_folder)
        print(f"Deleted folder {oldest_folder}")

    def monitor_folders(self):
        while True:
            for folder_path in self.folder_paths:
                files = self.get_file_list(folder_path)
                if len(files) > self.file_limit:
                    self.delete_oldest_file(files)

            folders = self.get_folder_list(self.monitored_folder)
            if len(folders) > self.folder_limit:
                self.delete_oldest_folder(folders)

            time.sleep(1)  # Check every second

    @staticmethod
    def monitor_Folder_runner():
        folder_paths = [
            "images/Axle Box Cover", "images/Axle Box Spring-Primary Suspention", "images/Bearing Assembly",
            "images/Bolster", "images/Bolster Spring-Secondary Suspention", "images/Bolster Suspention Hanger",
            "images/Brake Block", "images/Hanger Block", "images/Hanger Pin", "images/Load Bearing Springs",
            "images/Lower Spring Beam", "images/Primary Suspention", "images/Side Frame", "images/Spring Plank",
            "images/Track", "images/Vertical Damper", "images/Vertical Shock Absorber", "images/Wheel", "images/Yaw Damper"
        ]  # Add your folder paths here
        file_rotator = FileRotator(folder_paths)
        file_rotator.monitor_folders()

if __name__ == "__main__":
    FileRotator.monitor_Folder_runner()
