"""
FastAPI Backend Application for Supportlytics AI Agent System.
Provides RESTful endpoints for ticket processing, multi-agent tracing, HITL approvals, and analytics.
"""
import os
import asyncio
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional, List

from backend.database.store import db
from backend.agents.agent_system import orchestrator, generate_random_simulated_ticket

app = FastAPI(
    title="Supportlytics AI Agent API",
    description="Multi-Agent IT Support Ticket Intelligence System powered by Google ADK concepts, MCP, and Human-in-the-Loop governance.",
    version="1.0.0"
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Models
class TicketCreateRequest(BaseModel):
    title: str
    description: str
    user: Optional[str] = "Jane Doe (Staff Engineer)"

class HITLApprovalRequest(BaseModel):
    ticket_id: str
    approved: bool
    reviewer: str = "IT Operations Manager"
    comments: Optional[str] = "Reviewed via Supportlytics Governance Portal."

@app.get("/api/health")
def health_check():
    return {"status": "ONLINE", "system": "Supportlytics AI Engine", "adk_status": "ENABLED"}

@app.get("/api/tickets")
def get_tickets():
    """Returns all tickets sorted by creation date."""
    return {"tickets": db.get_all_tickets()}

@app.get("/api/tickets/{ticket_id}")
def get_ticket_details(ticket_id: str):
    ticket = db.get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"ticket": ticket, "trace": db.get_ticket_trace(ticket_id)}

@app.get("/api/tickets/{ticket_id}/trace")
def get_ticket_trace(ticket_id: str):
    return {"ticket_id": ticket_id, "trace": db.get_ticket_trace(ticket_id)}

@app.post("/api/tickets")
async def create_ticket(request: TicketCreateRequest):
    """Submits a new ticket for processing through the multi-agent pipeline."""
    ticket = await orchestrator.process_ticket(
        ticket_title=request.title,
        ticket_description=request.description,
        user_info=request.user
    )
    return {"ticket": ticket, "trace": db.get_ticket_trace(ticket["id"])}

@app.get("/api/hitl/queue")
def get_hitl_queue():
    """Retrieves all pending Human-in-the-Loop approval items."""
    return {"queue": db.get_hitl_queue()}

@app.post("/api/hitl/resolve")
def resolve_hitl(request: HITLApprovalRequest):
    """Processes a human approval or rejection decision."""
    result = db.resolve_hitl_action(
        ticket_id=request.ticket_id,
        approved=request.approved,
        reviewer=request.reviewer,
        comments=request.comments
    )
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result.get("error", "Error resolving action"))
    return result
@app.get("/api/analytics")
def get_analytics():
    """Returns system operational metrics and AI performance analytics."""
    return db.get_analytics()

class BulkTicketRequest(BaseModel):
    tickets: List[TicketCreateRequest]

@app.post("/api/tickets/bulk")
async def bulk_ingest(request: BulkTicketRequest, background_tasks: BackgroundTasks):
    async def process_all_bulk(tickets_list):
        for t in tickets_list:
            await orchestrator.process_ticket(t.title, t.description, t.user)
            await asyncio.sleep(0.5)
    background_tasks.add_task(process_all_bulk, request.tickets)
    return {"message": f"Successfully queued {len(request.tickets)} tickets for bulk processing."}

simulator_active = False

@app.post("/api/simulator/toggle")
async def toggle_simulator(background_tasks: BackgroundTasks):
    global simulator_active
    simulator_active = not simulator_active
    if simulator_active:
        background_tasks.add_task(run_simulator_loop)
    return {"simulator_active": simulator_active}

@app.get("/api/simulator/status")
def get_simulator_status():
    return {"simulator_active": simulator_active}

async def run_simulator_loop():
    global simulator_active
    print("Simulator Loop Started")
    while simulator_active:
        try:
            ticket_template = generate_random_simulated_ticket()
            await orchestrator.process_ticket(
                ticket_title=ticket_template["title"],
                ticket_description=ticket_template["description"],
                user_info=ticket_template["user"]
            )
        except Exception as e:
            print("Error in simulator loop:", e)
        await asyncio.sleep(12)
    print("Simulator Loop Stopped")

# Mount static frontend files if directory exists
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
