import os
import csv
import re

# Base directory
base_folder = "Vishal"

# Output CSV file
output_csv = "image_paths.csv"

# Allowed image extensions
image_extensions = ('.jpg', '.jpeg', '.webp')

# Natural sorting helper
def natural_key(text):
    return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', text)]

# Get all subfolders with natural sort
subfolders = sorted(
    [os.path.join(base_folder, f) for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))],
    key=natural_key
)

# Write to CSV
with open(output_csv, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    for folder in subfolders:
        # Get image files in natural order
        images = sorted(
            [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(image_extensions)],
            key=natural_key
        )

        for image_path in images:
            writer.writerow([image_path])

        writer.writerow([])  # Blank line

print(f"CSV file '{output_csv}' has been created with images in natural numeric order.")
