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

developer_id=$1 # Store developer_id from the argument
src_dir="submissions/template"
dest_dir="submissions/developer-${developer_id}"
branch_name="developer-${developer_id}-solution"

# Create the destination directory if it doesn't exist
mkdir -p "$dest_dir"

# Iterate over the files and directories in the source directory
for item in "$src_dir"/*; do
    # If the item is the config directory, only copy the developer-<id>.json file
    if [ "$(basename "$item")" = "config" ]; then
        mkdir -p "$dest_dir/config/"
        cp "$item/developer-${developer_id}.json" "$dest_dir/config/"
    else
        # Otherwise, copy the entire item
        cp -r "$item" "$dest_dir/"
    fi
done

# Initialize git if it's not already a git repository
if [ ! -d .git ]; then
    git init
fi

# Checkout to a new branch
git checkout -b "$branch_name"

# Add and commit the changes
git add .
git commit -m "Initial commit for developer ${developer_id}"

# Push the new branch to the remote repository
git push -u origin "$branch_name"

# Create a pull request using GitHub CLI (gh) or GitHub API
gh pr create --base main --head "$branch_name" --title "Solution PR for developer ${developer_id}" --body "Solution PR for developer ${developer_id}."
