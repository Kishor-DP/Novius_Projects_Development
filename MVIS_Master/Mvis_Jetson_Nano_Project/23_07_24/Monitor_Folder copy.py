import os
import time

class FileRotator:
    def __init__(self, folder_paths, file_limit=500):
        self.folder_paths = folder_paths
        self.file_limit = file_limit

    def get_file_list(self, folder_path):
        files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
        files = [f for f in files if os.path.isfile(f)]
        return files

    def delete_oldest_file(self, files):
        oldest_file = min(files, key=os.path.getctime)
        os.remove(oldest_file)
        print(f"Deleted {oldest_file}")

    def monitor_folders(self):
        while True:
            for folder_path in self.folder_paths:
                files = self.get_file_list(folder_path)
                if len(files) > self.file_limit:
                    self.delete_oldest_file(files)
            time.sleep(1)  # Check every second

if __name__ == "__main__":
    folder_paths = ["images/Axle Box Cover", "images/Axle Box Spring-Primary Suspention","images/Bearing Assembly",
                    "images/Bolster","images/Bolster Spring-Secondary Suspention","images/Bolster Suspention Hanger","images/Brake Block",
                    "images/Hanger Block","images/Hanger Pin","images/Load Bearing Springs",
                    "images/Lower Spring Beam","images/Primary Suspention","images/Side Frame",
                    "images/Spring Plank","images/Track","images/Vertical Damper","images/Vertical Shock Absorber",
                    "images/Wheel","images/Yaw Damper"]  # Add your folder paths here
    file_rotator = FileRotator(folder_paths)
    file_rotator.monitor_folders()
