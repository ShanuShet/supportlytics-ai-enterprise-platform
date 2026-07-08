from backend.websocket.event_publisher import publish


async def ticket_created(ticket):

    await publish(

        "ticket_created",

        ticket

    )


async def ticket_updated(ticket):

    await publish(

        "ticket_updated",

        ticket

    )


async def dashboard_refresh(data):

    await publish(

        "dashboard_refresh",

        data

    )