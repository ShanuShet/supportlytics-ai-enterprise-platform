from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.services.prediction_service import PredictionService

router = APIRouter(
    prefix="/prediction",
    tags=["AI Prediction"]
)


@router.get("/priority/{ticket_id}")
def predict_priority(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    service = PredictionService(db)

    result = service.predict_priority(ticket_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return result


@router.get("/risk/{ticket_id}")
def predict_risk(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    service = PredictionService(db)

    result = service.predict_risk(ticket_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return result


@router.get("/sla/{ticket_id}")
def predict_sla(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    service = PredictionService(db)

    result = service.predict_sla(ticket_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return result


@router.get("/resolution/{ticket_id}")
def predict_resolution(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    service = PredictionService(db)

    result = service.predict_resolution(ticket_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return result


@router.get("/all/{ticket_id}")
def predict_all(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    service = PredictionService(db)

    priority = service.predict_priority(ticket_id)

    if not priority:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    risk = service.predict_risk(ticket_id)

    sla = service.predict_sla(ticket_id)

    resolution = service.predict_resolution(ticket_id)

    return {

        "ticket_id": ticket_id,

        "priority": priority,

        "risk": risk,

        "sla": sla,

        "resolution": resolution

    }

@router.get("/recommendation/{ticket_id}")
def recommendation(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    service = PredictionService(db)

    result = service.predict_all(ticket_id)

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return result