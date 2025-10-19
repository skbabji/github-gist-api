# GitHub Gists API Service

## Overview
A simple FastAPI service in Python 3.13 that exposes `/USERNAME` endpoint to list public GitHub gists for a user. Packaged in a secure, minimal Docker container.

## Project Structure
```
.
├── app/
│   ├── main.py         # FastAPI app
│   ├── github.py       # GitHub API logic
│   └── __init__.py
├── tests/
│   ├── test_main.py    # Pytest tests
│   └── __init__.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .coveragerc
├── test-and-build.sh   # All-in-one setup, test, security, and build script
├── PROJECT_README.md   # This file
```

## Features
- FastAPI web server
- `/USERNAME` endpoint returns public gists for any GitHub user
- `/health` endpoint for health checks
- Automated tests with pytest and coverage
- Multi-stage Dockerfile (minimal, non-root user, parameterized Python version)
- Static and security analysis with Bandit

## Quick Start (Recommended)

Use the provided script to automate setup, testing, security analysis, and Docker build:

```sh
bash test-and-build.sh
```

This will:
- Create and activate a Python 3.13 virtual environment
- Install all dependencies
- Run tests with coverage
- Run Bandit security analysis
- Build the Docker image



## Run Locally (Without Docker)

### 1. Create and activate Python virtual environment
```sh
python3.13 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the FastAPI app
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

### 4. Test the API
```sh
curl "http://localhost:8080/octocat"
curl "http://localhost:8080/health"
```

## Manual Usage (Step-by-Step)

### 1. Create and activate Python virtual environment
```sh
python3.13 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```sh
pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt
```

### 3. Run tests with coverage
```sh
pytest --cov=app
```

### 4. Run Bandit security analysis
```sh
bandit -r app
```

### 5. Build Docker image
```sh
# Optionally set Python version (default: 3.13)
docker build --build-arg PYTHON_VERSION=3.13 -t gists-api .
```

### 6. Run Docker container
```sh
docker run -p 8080:8080 gists-api
```

### 7. Query API endpoints
```sh
curl "http://localhost:8080/octocat"
curl "http://localhost:8080/health"
```

## Notes
- No global/system installs required
- No root user in container
- Minimal image size
- Easy Python version upgrade via Docker build arg
