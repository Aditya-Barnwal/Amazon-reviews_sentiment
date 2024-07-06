import gdown
import os
import time

def download_model(max_retries=3):
    file_id = '1ugXcwXEHBUv7OfD7Cl7_LhbFRxruao3J'
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'roberta_model.sav'
    
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1} of {max_retries}")
        print(f"Attempting to download file from Google Drive...")
        try:
            gdown.download(url, output, quiet=False, fuzzy=True)
            
            if os.path.exists(output):
                file_size = os.path.getsize(output) / (1024 * 1024)  
                print(f"Downloaded file size: {file_size:.2f} MB")
                
                if file_size < 400:  
                    print("Warning: The downloaded file is smaller than expected.")
                else:
                    print("File downloaded successfully and size looks correct.")
                return
            else:
                print("Error: File was not downloaded successfully.")
        except Exception as e:
            print(f"An error occurred during download: {e}")
            if attempt < max_retries - 1:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Max retries reached. Download failed.")

if __name__ == "__main__":
    download_model()