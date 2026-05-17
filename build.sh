#!/bin/bash

echo "Building Docker image..."

docker build -t instance-counter .

echo "Running container..."

docker run --rm instance-counter