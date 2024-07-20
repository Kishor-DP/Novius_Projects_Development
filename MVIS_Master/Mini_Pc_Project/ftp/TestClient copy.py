from ftplib import FTP
import os

def upload_image_to_server(image_path, server_ip, username, password):
    ftp = None  # Initialize ftp to None
    try:
        # Check if the file exists
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"The file at {image_path} does not exist.")
        
        # Connect to the FTP server
        ftp = FTP(server_ip)
        ftp.login(user=username, passwd=password)
        
        # Open the image file in binary mode for uploading
        with open(image_path, 'rb') as file:
            # Extract the filename from the path
            filename = os.path.basename(image_path)
            # Upload the image to the server 
            ftp.storbinary(f'STOR {filename}', file)
        
        print("Image uploaded successfully")
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

# Replace these values with your actual credentials and image path
image_path = r'D:\trf_files\detected.jpg'
server_ip = '103.120.176.21'
username = 'noviusr1'
password = 'Yoj9IbR0y#M%'

upload_image_to_server(image_path, server_ip, username, password)
