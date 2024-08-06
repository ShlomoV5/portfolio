#!/bin/bash

# Function to create directories and files
create_structure() {
    local base_dir=""

    while IFS= read -r line; do
        # Remove leading and trailing whitespace
        line=$(echo "$line" | xargs)

        # Skip empty lines
        if [ -z "$line" ]; then
            continue
        fi

        # Calculate the indentation level
        indent_level=$(echo "$line" | sed -e 's/[^ ]//g' | wc -c)
        indent_level=$((indent_level / 4))

        # Remove leading indentation and '│', '├──', '└──'
        line=$(echo "$line" | sed -e 's/^[ │├└─]*//')

        # Construct the path
        if [[ "$line" == */ ]]; then
            base_dir=$(printf "%*s" $((indent_level * 4)) | tr ' ' '/')
            mkdir -p "$base_dir$line"
            echo "Created directory: $base_dir$line"
        else
            file_path=$(printf "%*s" $((indent_level * 4)) | tr ' ' '/')
            touch "$file_path$line"
            echo "Created file: $file_path$line"
        fi
    done < "$1"
}

# Check if input file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <structure_file>"
    exit 1
fi

# Create the file structure
create_structure "$1"