import os
import re

class FolderManager:
    def __init__(self, base_path, root_folder, subfolder_count, second_subfolder_name="Train_Video"):
        self.base_path = base_path
        self.root_folder = self.sanitize_folder_name(root_folder)
        # Default to 1 subfolder with the name root_folder + "_sub" if no count is provided
        self.subfolder_count = subfolder_count if subfolder_count > 0 else 1
        self.subfolder_name = f"{self.root_folder}_Coach_1" if subfolder_count <= 0 else None
        self.second_subfolder_name = self.sanitize_folder_name(second_subfolder_name)
    
    def sanitize_folder_name(self, name):
        # Replace disallowed characters with underscores
        return re.sub(r'[:*?"<>|]', '_', name)
    
    def create_folders(self):
        # Create the root folder if it doesn't exist
        root_folder_path = os.path.join(self.base_path, self.root_folder)
        print(f"Creating root folder: {root_folder_path}")
        if not os.path.exists(root_folder_path):
            os.makedirs(root_folder_path)
            print(f"Root folder '{root_folder_path}' created.")
        else:
            print(f"Root folder '{root_folder_path}' already exists.")

        # Create the fixed "Train Video" folder directly under the root folder
        second_subfolder_path = os.path.join(root_folder_path, self.second_subfolder_name)
        print(f"Creating second subfolder: {second_subfolder_path}")
        if not os.path.exists(second_subfolder_path):
            os.makedirs(second_subfolder_path)
            print(f"Subfolder '{self.second_subfolder_name}' created inside '{root_folder_path}'.")
        else:
            print(f"Subfolder '{self.second_subfolder_name}' already exists inside '{root_folder_path}'.")

        for i in range(self.subfolder_count):
            # Determine the first subfolder name
            first_subfolder_name = self.subfolder_name if self.subfolder_name else input(f"Enter the name for first subfolder {i+1}: ")
            first_subfolder_name = self.sanitize_folder_name(first_subfolder_name)

            first_subfolder_path = os.path.join(root_folder_path, first_subfolder_name)
            print(f"Creating first subfolder: {first_subfolder_path}")
            if not os.path.exists(first_subfolder_path):
                os.makedirs(first_subfolder_path)
                print(f"Subfolder '{first_subfolder_name}' created inside '{root_folder_path}'.")
            else:
                print(f"Subfolder '{first_subfolder_name}' already exists inside '{root_folder_path}'.")

            # Create subfolders "Coach Images" and "OCR images-3 images for each coach" inside the first subfolder
            ax_path = os.path.join(first_subfolder_path, "Coach Images")
            by_path = os.path.join(first_subfolder_path, "OCR images-3 images for each coach")
            new_static_folder_path = os.path.join(first_subfolder_path, "Component Images")
            
            print(f"Creating subfolder: {ax_path}")
            if not os.path.exists(ax_path):
                os.makedirs(ax_path)
                print(f"Subfolder 'Coach Images' created inside '{first_subfolder_name}'.")
            else:
                print(f"Subfolder 'Coach Images' already exists inside '{first_subfolder_name}'.")

            print(f"Creating subfolder: {by_path}")
            if not os.path.exists(by_path):
                os.makedirs(by_path)
                print(f"Subfolder 'OCR images-3 images for each coach' created inside '{first_subfolder_name}'.")
            else:
                print(f"Subfolder 'OCR images-3 images for each coach' already exists inside '{first_subfolder_name}'.")

            print(f"Creating subfolder: {new_static_folder_path}")
            if not os.path.exists(new_static_folder_path):
                os.makedirs(new_static_folder_path)
                print(f"Subfolder 'Component Images' created inside '{first_subfolder_name}'.")
            else:
                print(f"Subfolder 'Component Images' already exists inside '{first_subfolder_name}'.")

            # Create subfolder "stitched coach images" inside the "Coach Images" folder
            axx_path = os.path.join(ax_path, "stitched coach images")
            
            print(f"Creating subfolder: {axx_path}")
            if not os.path.exists(axx_path):
                os.makedirs(axx_path)
                print(f"Subfolder 'stitched coach images' created inside 'Coach Images'.")
            else:
                print(f"Subfolder 'stitched coach images' already exists inside 'Coach Images'.")

if __name__ == "__main__":
    # Get user inputs
    base_path = "D:\\main"#input("Enter the base path where the folders should be created: ")
    root_folder = input("Enter the name of the root folder: ")
    subfolder_input = input("Enter the number of first subfolders to create (press Enter to create 1): ")
    subfolder_count = int(subfolder_input) if subfolder_input else 0  # Use 0 to trigger default behavior

    folder_manager = FolderManager(base_path, root_folder, subfolder_count)
    folder_manager.create_folders()
