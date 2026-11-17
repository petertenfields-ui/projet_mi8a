#TODO:make a websocket connection to get data to fastapi
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
router = APIRouter()
connections : set[WebSocket] = set()
@router.websocket("/ws/audio")
async def receive_audio(websocket:WebSocket):
    #Envoi de l'audio
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            disconnected = []
            for browser in connections:
                try:
                    await browser.send_json(data)
                except Exception:
                    disconnected += [browser]
            for browser in disconnected:
                connections.discard(browser)
    except WebSocketDisconnect:
        print("Disconnected")

@router.websocket("/ws/visual")
async def visualisation(websocket:WebSocket):
    await websocket.accept()
    connections.add(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connections.discard(websocket)