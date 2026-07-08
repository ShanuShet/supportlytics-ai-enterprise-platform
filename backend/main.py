from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import websocket
from backend.api.analytics import router as analytics_router
from backend.api.tickets import router as tickets_router
from backend.api.dashboard import router as dashboard_router
from backend.api.ingestion import router as ingestion_router
from backend.api.prediction import router as prediction_router
from backend.api.simulator import router as simulator_router

from backend.database.init_db import initialize_database

# Create FastAPI application
app = FastAPI(
    title="Supportlytics AI",
    description="Enterprise Intelligent IT Operations Platform",
    version="2.0.0"
)

# Startup Event
@app.on_event("startup")
def startup():
    initialize_database()
    print("Database initialized successfully.")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(analytics_router)
app.include_router(tickets_router)
app.include_router(dashboard_router)
app.include_router(ingestion_router)
app.include_router(prediction_router)
app.include_router(simulator_router)
app.include_router(websocket.router)

# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "Supportlytics AI API Running",
        "version": "2.0.0",
        "status": "Healthy"
    }

