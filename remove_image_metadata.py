import os
import subprocess
from pathlib import Path

def remove_metadata(input_folder, output_folder):
    input_folder = Path(input_folder).resolve()
    output_folder = Path(output_folder).resolve()
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")

    output_folder.mkdir(parents=True, exist_ok=True)

    supported_formats = ['.jpg', '.jpeg', '.png', '.webp', '.tiff', '.bmp', '.heic']

    for img_file in input_folder.iterdir():
        if img_file.suffix.lower() in supported_formats:
            output_file = output_folder / img_file.name
            print(f"Processing: {img_file.name} → {output_file.name}")

            try:
                result = subprocess.run([
                    "exiftool",
                    "-all=",
                    "-o", str(output_file),
                    str(img_file)
                ], check=True, capture_output=True, text=True)

                print(result.stdout)
                print(f"✅ Metadata removed: {output_file.name}")

            except subprocess.CalledProcessError as e:
                print(f"❌ Error processing {img_file.name}:\n{e.stderr}")

if __name__ == "__main__":
    input_dir = "e"
    output_dir = "r"

    remove_metadata(input_dir, output_dir)
