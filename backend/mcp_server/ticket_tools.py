from backend.database.store import db


def get_ticket(ticket_id):

    return db.get_ticket(ticket_id)


def get_all_tickets():

    return db.get_all_tickets()