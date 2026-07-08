class PermissionManager:

    ROLES = {

        "ADMIN": [
            "read",
            "write",
            "delete",
            "approve"
        ],

        "ANALYST": [
            "read",
            "write"
        ],

        "VIEWER": [
            "read"
        ]
    }

    @classmethod
    def has_permission(
        cls,
        role: str,
        permission: str
    ):

        return permission in cls.ROLES.get(
            role,
            []
        )