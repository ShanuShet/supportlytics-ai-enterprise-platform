import random

CATEGORIES = [
    "Network & Infrastructure",
    "IAM & Access Management",
    "Hardware & Peripherals",
    "Software & Applications"
]

PRIORITIES = [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]

USERS = [
    "John Doe",
    "Sarah Jenkins",
    "David Miller",
    "Emily Clark",
    "Michael Scott"
]

DEPARTMENTS = [
    "Finance",
    "Engineering",
    "HR",
    "Operations",
    "IT"
]


class TicketGenerator:

    @staticmethod
    def generate():

        category = random.choice(CATEGORIES)

        return {

            "title": f"{category} Issue",

            "description": f"Automatically generated {category} incident.",

            "category": category,

            "priority": random.choice(PRIORITIES),

            "user": random.choice(USERS),

            "department": random.choice(DEPARTMENTS)

        }