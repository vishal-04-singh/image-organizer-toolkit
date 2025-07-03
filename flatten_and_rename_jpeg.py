import os
import shutil

# Change this to your base directory
base_dir = "/Users/vishal04/Developer/META/Vivek"

# Loop through all main folders (e.g., 7, 31)
for main_folder in os.listdir(base_dir):
    main_folder_path = os.path.join(base_dir, main_folder)
    if os.path.isdir(main_folder_path):
        # Loop through subfolders like "2Y, N", "10Y, O", etc.
        for subfolder in os.listdir(main_folder_path):
            subfolder_path = os.path.join(main_folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                # Decide prefix from subfolder name
                if "N" in subfolder:
                    prefix = "N"
                elif "O" in subfolder:
                    prefix = "O"
                else:
                    print(f"Skipping unknown type folder: {subfolder}")
                    continue

                count = 1
                for filename in sorted(os.listdir(subfolder_path)):
                    file_path = os.path.join(subfolder_path, filename)
                    if filename.lower().endswith(".jpeg"):
                        new_name = f"{prefix}_{count}.jpg"
                        new_path = os.path.join(main_folder_path, new_name)
                        print(f"Moving + Renaming: {file_path} → {new_path}")
                        shutil.move(file_path, new_path)
                        count += 1

                # Try to delete subfolder after moving
                try:
                    os.rmdir(subfolder_path)
                    print(f"Deleted folder: {subfolder_path}")
                except OSError as e:
                    print(f"Could not delete folder {subfolder_path}: {e}")
