#!/bin/bash

# Specify the folder path containing text files
TEXT_FOLDER_PATH="/home/ocr_project/tesstrain/data/eval_data-ground-truth"

# Ensure the folder exists
if [ ! -d "$TEXT_FOLDER_PATH" ]; then
  echo "Error: Folder not found."
  exit 1
fi

# Loop through each text file in the folder
for file in "$TEXT_FOLDER_PATH"/*.txt; do
  # Check if it's a file
  if [ -f "$file" ]; then
    # Reverse each character and preserve spaces, then overwrite the file
    cat "$file" | rev > "$file.tmp"
    mv "$file.tmp" "$file"
    echo "Reversed content in $file"
  fi
done

echo "Reversal complete."

