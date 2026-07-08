from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.services.simulator_service import SimulatorService

router = APIRouter(
    prefix="/simulator",
    tags=["Traffic Simulator"]
)


@router.post("/start")
def start_simulator(
    db: Session = Depends(get_db)
):

    service = SimulatorService(db)

    result = service.generate_tickets(10)

    return result


@router.post("/stop")
def stop_simulator():

    return {
        "status": "Simulator Stopped"
    }