from backend.database.store import db


def seed_database():

    print("Loading demo tickets...")

    print(f"{len(db.get_all_tickets())} demo tickets loaded.")


if __name__ == "__main__":
    seed_database()