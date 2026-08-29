from fastapi import FastAPI

app = FastAPI(
    title="Task API",
    description="A lightweight REST API for managing tasks, built with FastAPI and Dockerized for seamless container deployment",
    version="1.0.0"
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