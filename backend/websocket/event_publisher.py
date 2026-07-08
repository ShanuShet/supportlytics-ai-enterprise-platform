from backend.websocket.websocket_manager import manager


async def publish(event, data):

    await manager.broadcast({

        "event": event,

        "payload": data

    })