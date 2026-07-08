import logging

logging.basicConfig(
    filename="logs/security.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


class AuditLogger:

    @staticmethod
    def log(
        action: str,
        user: str
    ):

        logging.info(
            f"{user} -> {action}"
        )