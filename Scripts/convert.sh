#!/bin/bash

# Create the "mp4" directory if it doesn't exist
mkdir -p "mp4"

# Loop through all files in the current directory
for file in *; do
    # Check if the file has a .webm extension
    if [[ "$file" == *.webm ]]; then
        # Get the base filename without the extension
        base_name="${file%.*}"

        # Convert the WebM file to MP4 format
        ffmpeg -i "$file" -c:v libx264 -pix_fmt yuv420p -c:a aac "mp4/$base_name.mp4"
        
        # Print a message indicating the conversion
        echo "Converted $file to mp4/$base_name.mp4"
    fi
done