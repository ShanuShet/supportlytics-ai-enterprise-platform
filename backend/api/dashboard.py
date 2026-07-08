from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.session import get_db
from backend.dashboard.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(db: Session = Depends(get_db)):
    service = DashboardService(db)
    return service.get_dashboard()


@router.get("/live")
def live_dashboard(db: Session = Depends(get_db)):
    service = DashboardService(db)
    return service.get_dashboard()


@router.get("/metrics")
def metrics(db: Session = Depends(get_db)):
    service = DashboardService(db)
    return service.get_dashboard()["overview"]