import os
import shutil

# Base directory path
base_dir = "Vishal"

# Mapping of subfolders to naming prefix
prefix_map = {
    "n": "N",
    "2y": "N",
    "o": "O",
    "10y": "O"
}

# Loop through all main folders like 1, 2, 3...
for main_folder in sorted(os.listdir(base_dir)):
    main_folder_path = os.path.join(base_dir, main_folder)
    if os.path.isdir(main_folder_path):
        print(f"\nProcessing folder: {main_folder_path}")

        # Counters for renaming
        counters = {"N": 1, "O": 1}

        # Check each subfolder
        for subfolder in os.listdir(main_folder_path):
            subfolder_path = os.path.join(main_folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                key = subfolder.strip().lower()
                if key in prefix_map:
                    prefix = prefix_map[key]
                    print(f"  Found subfolder: {subfolder} → Using prefix: {prefix}")

                    # Process image files
                    for filename in sorted(os.listdir(subfolder_path)):
                        file_path = os.path.join(subfolder_path, filename)
                        if filename.lower().endswith(('.jpeg', '.jpg', '.webp')):
                            new_name = f"{prefix}_{counters[prefix]}.jpg"
                            new_path = os.path.join(main_folder_path, new_name)
                            print(f"    Renaming + Moving: {filename} → {new_name}")
                            shutil.move(file_path, new_path)
                            counters[prefix] += 1

                    # Delete the subfolder if empty
                    try:
                        os.rmdir(subfolder_path)
                        print(f"  Deleted empty subfolder: {subfolder_path}")
                    except OSError as e:
                        print(f"  Failed to delete folder {subfolder_path}: {e}")
