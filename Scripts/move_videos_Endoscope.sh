#!/bin/bash

# Source and destination directories
SOURCE_DIR=~/Downloads
DEST_DIR="/media/administrator/New Volume/Recordings_Backup"

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Find and move video files
find "$SOURCE_DIR" -type f \( -iname "*.mp4" -o -iname "*.mkv" -o -iname "*.avi" -o -iname "*.webm" \) -exec cp {} "$DEST_DIR" \;
