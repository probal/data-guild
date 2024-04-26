#!/bin/bash

# Get the absolute path of the current script
script_dir=$(dirname "$(realpath "$0")")

# Check the parameter
if [ "$1" == "build" ]; then
    # Docker build command
    docker buildx build -t prefect --platform=linux/amd64 .
elif [ "$1" == "orion" ]; then
    # Run Orion Server
    docker-compose --profile orion up
elif [ "$1" == "cli" ]; then
    # Run CLI
    docker-compose run cli
elif [ "$1" == "agent" ]; then
    # Run Agent
    docker-compose --profile agent up
elif [ "$1" == "deploy" ]; then
    # Iterate over all Python scripts in the flows directory
    for file in "$script_dir"/flows/*.py; do
        # Extract the base name of the file (without directory and extension)
        base_name=$(basename "$file" .py)
        echo "Deploying $file"
        # Create a deployment for the script
        prefect deployment build -n default -q default -a "$file:$base_name"
    done
else
    echo "Invalid parameter. Please use 'build', 'orion', 'cli', 'agent', 'deploy'."
fi