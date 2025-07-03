import os
import csv

# Base directory
base_folder = "Vishal"

# Output CSV file
output_csv = "image_paths.csv"

# Allowed image extensions (case-insensitive)
image_extensions = ('.jpg', '.jpeg', '.webp')

# Get all subfolders and sort them in ascending order
subfolders = sorted(
    [os.path.join(base_folder, f) for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
)

# Write to CSV
with open(output_csv, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    for folder in subfolders:
        # Get all valid image files in ascending order
        images = sorted(
            [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(image_extensions)]
        )

        # Write image paths
        for image_path in images:
            writer.writerow([image_path])

        # Write a blank line after each folder
        writer.writerow([])

print(f"CSV file '{output_csv}' has been created with all supported image types in ascending order.")
