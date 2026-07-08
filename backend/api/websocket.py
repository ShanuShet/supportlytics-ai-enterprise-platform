from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.websocket.websocket_manager import manager

router = APIRouter(tags=["WebSocket"])


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:

        while True:

            message = await websocket.receive_text()

            if message == "ping":

                await websocket.send_json(
                    {
                        "event": "pong"
                    }
                )

    except WebSocketDisconnect:

        manager.disconnect(websocket)