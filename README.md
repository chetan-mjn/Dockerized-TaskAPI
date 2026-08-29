# Dockerized Task API

A lightweight RESTful API built with FastAPI, designed to manage tasks and serve as a hands-on project for learning containerization with Docker and Docker Compose.

## Features

* **Task Management**: Simple REST endpoints to manage tasks.
* **FastAPI**: Modern, fast Python web framework with auto-generated OpenAPI documentation.
* **Dockerized Environment**: Easily reproducible local setup using Docker and Docker Compose.

## Project Structure

```text
docker-task-api/
├── app/
│   ├── __init__.py
│   └── main.py
├── .dockerignore
├── compose.yaml
├── Dockerfile
├── README.md
└── requirements.txt