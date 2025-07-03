# Image Utils 🖼️

A collection of Python utilities for managing and processing image files efficiently.

## Overview

This repository contains a set of Python scripts designed to help you manage, organize, and process image files. Each script serves a specific purpose in the image management workflow.

## Scripts

### 1. Flatten and Rename JPEG Files (`flatten_and_rename_jpeg.py`)

A utility to simplify your image directory structure and standardize file naming.

#### Features
- Flattens nested directory structures containing JPEG files
- Implements consistent file naming patterns
- Automatically removes empty directories after moving files
- Preserves original file order during processing

#### Usage
```bash
python3 flatten_and_rename_jpeg.py
```

### 2. Generate Image CSV (`generate_image_csv.py`)

Creates a comprehensive CSV inventory of your image files.

#### Features
- Generates a CSV file listing all image paths
- Supports multiple image formats:
  - .jpg
  - .jpeg
  - .webp
- Organizes paths by folder with clear separators
- Maintains alphabetical ordering

#### Usage
```bash
python3 generate_image_csv.py
```

### 3. Remove Image Metadata (`remove_metadata.py`)

Cleanses images of metadata while preserving image quality.

#### Features
- Removes all metadata from images using ExifTool
- Supports multiple image formats:
  - .jpg/.jpeg
  - .png
  - .webp
  - .tiff
  - .bmp
  - .heic
- Creates clean copies in a separate output directory
- Preserves original files

#### Usage
```bash
python3 remove_metadata.py
```

## Requirements

### System Requirements
- Python 3.x
- ExifTool (required for metadata removal)

### Python Dependencies
All scripts use standard Python libraries:
- os
- shutil
- csv
- subprocess
- pathlib

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vishal-04-singh/image-utils.git
cd image-utils
```

2. Install ExifTool (if you plan to use metadata removal):
   - **macOS**: `brew install exiftool`
   - **Linux**: `sudo apt-get install exiftool`
   - **Windows**: Download from [ExifTool website](https://exiftool.org/)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Last Updated
2025-07-03

## Author
[@vishal-04-singh](https://github.com/vishal-04-singh)

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/vishal-04-singh/image-utils/issues).