import uuid


def generate_ticket_id():

    return f"TICK-{uuid.uuid4().hex[:8].upper()}"


def current_timestamp():

    from datetime import datetime

    return datetime.utcnow().isoformat()