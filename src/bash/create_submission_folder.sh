#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Error: Exactly one argument is required."
    exit 1
fi

# Check if the parameter is a number
if ! [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Error: The argument must be a number."
    exit 1
fi

coder_id=$1 #put your code id here
src_dir="submissions/template"
dest_dir="submissions/coder-${coder_id}"

# Create the destination directory if it doesn't exist
mkdir -p "$dest_dir"

# Iterate over the files and directories in the source directory
for item in "$src_dir"/*; do
    # If the item is the config directory, only copy the coder-<id>.json file
    if [ "$(basename "$item")" = "config" ]; then
        mkdir "$dest_dir/config/"
        cp "$item/coder-${coder_id}.json" "$dest_dir/config/"
    else
        # Otherwise, copy the entire item
        cp -r "$item" "$dest_dir/"
    fi
done