from ftplib import FTP
from time import sleep


# IP_ADDR = "87.248.153.134"
IP_ADDR = "127.0.0.1"

PORT = 21

def connect_ftp(server, username, password):
    try:
        # Connect to the FTP server
        ftp = FTP(server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {server}")

        return ftp
    except Exception as e:
        print(f"Failed to connect to FTP server: {e}")
        return None

def list_files(ftp,directory="."):
    try:
        files = ftp.nlst("..\masoud")  # List files and directories
        print("Files and directories on the server:")
        for file in files:
            print(f" - {file}")
    except Exception as e:
        print(f"Failed to list files: {e}")

def download_file(ftp, filename, local_path):
    try:
        with open(local_path, 'wb') as local_file:
            ftp.retrbinary(f"RETR {filename}", local_file.write)
        print(f"Downloaded {filename} to {local_path}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

def upload_file(ftp, local_path, filename):
    try:
        with open(local_path, 'rb') as local_file:
            ftp.storbinary(f"STOR {filename}", local_file)
        print(f"Uploaded {local_path} as {filename}")
    except Exception as e:
        print(f"Failed to upload {local_path}: {e}")

def main(): 
    # FTP server details
    server = IP_ADDR  # Change to your FTP server IP or hostname
    username = 'erfan'     # Change to your FTP username
    password = '123' # Change to your FTP password

    # Connect to the FTP server
    ftp = connect_ftp(server, username, password)
    if ftp is None:
        return

    # List files on the server
    list_files(ftp)
    
    print("sleep")
    sleep(3)

    # Example of downloading a file
    filename_to_download = 'a.txt'  # Change to the filename you want to download
    local_download_path = filename_to_download
    download_file(ftp, filename_to_download, local_download_path)

    print("sleep")
    sleep(3)
    
    # Example of uploading a file
    local_upload_path = 'b.txt'  # Change to your local file path
    filename_to_upload = local_upload_path
    upload_file(ftp, local_upload_path, filename_to_upload)

    print("sleep")
    sleep(3)
    # Close the FTP connection
    ftp.quit()

if __name__ == '__main__':
    main()
