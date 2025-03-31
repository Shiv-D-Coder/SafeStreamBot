#!/bin/bash

# image name
IMAGE_NAME="safestreambot"

# port mapping
PORT_MAPPING="8501:8501"

# Build the Docker image
echo "Building the Docker image..."
docker build -t ${IMAGE_NAME} .

# Check if the build was successful
if [ $? -eq 0 ]; then
  echo "Docker image built successfully."
else
  echo "Failed to build Docker image. Check the output for errors."
  exit 1
fi

# Run the Docker container
echo "Running the Docker container..."
docker run -p ${PORT_MAPPING} ${IMAGE_NAME}

# Check if the container started successfully
if [ $? -eq 0 ]; then
  echo "Docker container is running. Access the application at http://localhost:${PORT_MAPPING%%:*}"
else
  echo "Failed to run Docker container. Check the output for errors."
  exit 1
fi

exit 0
