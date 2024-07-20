from ftplib import FTP
import os

def upload_folder_to_server(folder_path, server_ip, username, password, remote_directory):
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

        # Walk through all files and directories in the folder
        for root, dirs, files in os.walk(folder_path):
            # Determine the path on the server
            relative_path = os.path.relpath(root, folder_path)
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

            # Upload files in the current directory
            for filename in files:
                local_file_path = os.path.join(root, filename)
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
folder_path = r'D:\MVIS Data'
server_ip = '103.120.176.21'
username = 'noviusr1'
password = 'Yoj9IbR0y#M%'
remote_directory = '/mvis.Noviusrailtech.com/MVIS Data'

upload_folder_to_server(folder_path, server_ip, username, password, remote_directory)
