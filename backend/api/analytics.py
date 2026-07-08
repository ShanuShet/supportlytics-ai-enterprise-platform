from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/overview")
def overview(db: Session = Depends(get_db)):

    service = AnalyticsService(db)

    return service.overview()


@router.get("/categories")
def categories(db: Session = Depends(get_db)):

    service = AnalyticsService(db)

    return service.categories()


@router.get("/kpis")
def kpis(db: Session = Depends(get_db)):

    service = AnalyticsService(db)

    return service.priorities()


@router.get("/countries")
def countries(db: Session = Depends(get_db)):

    service = AnalyticsService(db)

    return service.countries()


@router.get("/trends")
def trends():

    return [
        {
            "date": "2026-07-01",
            "tickets": 6
        }
    ]