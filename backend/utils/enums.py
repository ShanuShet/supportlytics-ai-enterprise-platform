from enum import Enum


class TicketStatus(str, Enum):

    PROCESSING = "PROCESSING"

    RESOLVED = "RESOLVED"

    PENDING_APPROVAL = "PENDING_APPROVAL"

    BLOCKED = "BLOCKED_SECURITY_VIOLATION"


class Priority(str, Enum):

    LOW = "LOW"

    MEDIUM = "MEDIUM"

    HIGH = "HIGH"

    CRITICAL = "CRITICAL"