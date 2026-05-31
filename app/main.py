from fastapi import FastAPI  
from prometheus_fastapi_instrumentator import Instrumentator  
from datetime import datetime

app = FastAPI(
    title="Observability POC",
    description="FastAPI service for Kubernetes, Prometheus and Grafana monitoring",
    version="1.0.0"
)

# Enable Prometheus metrics endpoint
Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {
        "message": "Observability POC Service",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/info")
def info():
    return {
        "service": "observability-poc",
        "version": "1.0.0",
        "environment": "development"
    }