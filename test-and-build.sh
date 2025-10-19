#!/bin/bash
set -e

# Create and activate virtual environment
python3.13 -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt

# Run tests with coverage
pytest --cov=app

# Run security analysis
bandit -r app

# Build Docker image
DOCKER_TAG=gists-api
PYTHON_VERSION=3.13

docker build --build-arg PYTHON_VERSION=$PYTHON_VERSION -t $DOCKER_TAG .

echo "\nAll steps completed successfully!"
