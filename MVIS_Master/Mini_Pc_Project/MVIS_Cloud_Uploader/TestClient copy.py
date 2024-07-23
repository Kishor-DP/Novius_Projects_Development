from ftplib import FTP
import os
import json

def get_code_from_config(config_path):
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"The config file at {config_path} does not exist.")
    
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
        return config.get('Code')

def upload_folder_to_server(folder_path, server_ip, username, password, remote_directory, target_code):
    ftp = None  # Initialize ftp to None
    try:
        # Check if the folder exists
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"The folder at {folder_path} does not exist.")
        
        # Connect to the FTP server
        ftp = FTP(server_ip)
        ftp.login(user=username, passwd=password)
        
        # Change to the specified directory on the server
        ftp.cwd(remote_directory)
        
        # Get the list of directories in the folder_path
        folder_names = next(os.walk(folder_path))[1]

        if target_code not in folder_names:
            raise FileNotFoundError(f"No folder matching the code '{target_code}' found in {folder_path}.")

        # Path of the folder to be uploaded
        dir_path = os.path.join(folder_path, target_code)
        relative_path = os.path.relpath(dir_path, folder_path)
        server_path = os.path.join(remote_directory, relative_path).replace("\\", "/")
        
        # Create directories on the server if they do not exist
        try:
            ftp.cwd(server_path)
        except:
            # If changing directory fails, try creating it
            base_dir = remote_directory
            for part in relative_path.split(os.sep):
                base_dir = os.path.join(base_dir, part).replace("\\", "/")
                try:
                    ftp.cwd(base_dir)
                except:
                    ftp.mkd(base_dir)
                    ftp.cwd(base_dir)

        # Upload files in the target directory
        for filename in os.listdir(dir_path):
            local_file_path = os.path.join(dir_path, filename)
            if os.path.isfile(local_file_path):
                with open(local_file_path, 'rb') as file:
                    # Upload the file to the server
                    ftp.storbinary(f'STOR {filename}', file)
                    print(f"Uploaded {filename} to {server_path} successfully")
                
    except FileNotFoundError as fnf_error:
        print("File not found error:", fnf_error)
    except PermissionError as perm_error:
        print("Permission error:", perm_error)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the FTP connection if it was established
        if ftp:
            ftp.quit()

# Replace these values with your actual credentials and folder path
folder_path = r'D:\Novius\MVIS_Cloud_Uploader'
server_ip = '103.120.176.21'
username = 'noviusr1'
password = 'Yoj9IbR0y#M%'
remote_directory = '/mvis.Noviusrailtech.com/MVIS Data'
config_path = os.path.join(folder_path, 'config1.json')

try:
    target_code = get_code_from_config(config_path)
    print(f"Target code from config1.json: {target_code}")
    upload_folder_to_server(folder_path, server_ip, username, password, remote_directory, target_code)
except Exception as e:
    print("An error occurred:", e)
