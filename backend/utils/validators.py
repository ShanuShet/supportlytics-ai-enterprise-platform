def validate_ticket(ticket):

    required = [

        "title",

        "description"

    ]

    missing = [

        field

        for field in required

        if field not in ticket

    ]

    return {

        "valid": len(missing) == 0,

        "missing_fields": missing

    }