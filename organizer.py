import os
import shutil
folder_path = "C:/Users/tosin/Downloads"
file_types = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".docx"],
    "Videos": [".mp4", ".mkv"]
    }
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            
            if filename.endswith(tuple(extensions)):
                
                folder_dir = os.path.join(folder_path, folder)
                
                if not os.path.exists(folder_dir):
                    os.makedirs(folder_dir)
                    
                    shutil.move(file_path, os.path.join(folder_dir, filename))
        
                    
