import os
import shutil

# Change this to your base directory
base_dir = "/Users/vishal04/Developer/META/Vivek"

# Loop through all main folders (e.g., 7, 31)
for main_folder in os.listdir(base_dir):
    main_folder_path = os.path.join(base_dir, main_folder)
    if os.path.isdir(main_folder_path):
        # Loop through subfolders like N, O
        for subfolder in os.listdir(main_folder_path):
            subfolder_path = os.path.join(main_folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                count = 1
                for filename in sorted(os.listdir(subfolder_path)):
                    file_path = os.path.join(subfolder_path, filename)
                    if filename.lower().endswith(".jpeg"):
                        new_name = f"{subfolder}_{count}.jpg"
                        new_path = os.path.join(main_folder_path, new_name)
                        print(f"Moving + Renaming: {file_path} → {new_path}")
                        shutil.move(file_path, new_path)
                        count += 1

                # After moving all files, delete the empty subfolder
                try:
                    os.rmdir(subfolder_path)
                    print(f"Deleted folder: {subfolder_path}")
                except OSError as e:
                    print(f"Could not delete folder {subfolder_path}: {e}")

# For Run - python3 /Users/vishal04/Developer/META/flatten_and_rename_jpeg.py