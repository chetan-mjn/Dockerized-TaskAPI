from fastapi import FastAPI
import os

app_name = os.getenv("APP_NAME", "Task API")
app_version = os.getenv("APP_VERSION", "1.0.0")

app = FastAPI(
    title=app_name,
    description="A lightweight REST API for managing tasks, built with FastAPI and Dockerized for seamless container deployment",
    version=app_version
)

@app.get("/")
def root():
    return {
        "message" : "Task API is running"
    }

@app.get("/health")
def check_health():
    return {
        "status" : "healthy"
    }