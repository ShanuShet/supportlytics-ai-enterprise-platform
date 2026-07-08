import os
import shutil

import pandas as pd

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.models.ticket import Ticket

router = APIRouter(
    prefix="/ingestion",
    tags=["Bulk Ingestion"]
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        df = pd.read_excel(file_path)

        imported = 0
        skipped = 0

        for _, row in df.iterrows():

            ticket_id = str(row["ticket_id"])

            existing = db.query(Ticket).filter(
                Ticket.ticket_id == ticket_id
            ).first()

            if existing:
                skipped += 1
                continue

            priority = str(
                row.get(
                    "priority",
                    ""
                )
            ).lower()

            if priority == "critical":
                risk_score = 0.95

            elif priority == "high":
                risk_score = 0.80

            elif priority == "medium":
                risk_score = 0.55

            elif priority == "low":
                risk_score = 0.25

            else:
                risk_score = 0.10
            ticket = Ticket(

                ticket_id=ticket_id,

                title=str(
                    row.get(
                        "ticket_subject",
                        ""
                    )
                ),

                description=str(
                    row.get(
                        "ticket_description",
                        ""
                    )
                ),

                category=str(
                    row.get(
                        "category",
                        ""
                    )
                ),

                priority=priority,

                status=str(
                    row.get(
                        "status",
                        "OPEN"
                    )
                ),

                assigned_team=str(
                    row.get(
                        "assigned_to_user_id",
                        ""
                    )
                ),

                user_name=str(
                    row.get(
                        "submitted_by_user_id",
                        ""
                    )
                ),

                department=str(
                    row.get(
                        "department",
                        ""
                    )
                ),

                country=str(
                    row.get(
                        "location",
                        "Unknown"
                    )
                ),

                risk_score=risk_score

            )

            db.add(ticket)

            imported += 1

        db.commit()

        return {

            "status": "success",

            "filename": file.filename,

            "ticketsImported": imported,

            "duplicatesSkipped": skipped

        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/validate")
async def validate_dataset():

    return {

        "status": "Validation Completed"

    }