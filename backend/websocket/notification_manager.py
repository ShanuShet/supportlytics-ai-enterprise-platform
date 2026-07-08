from backend.websocket.event_publisher import publish


async def send_notification(message):

    await publish(

        "notification",

        {

            "message": message

        }

    )