#TODO:make a websocket connection to get data to fastapi
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
router = APIRouter()
connections : set[WebSocket] = set()
@router.websocket("/ws/audio")
async def receive_audio(websocket:WebSocket):
    #Envoi de l'audio
    await websocket.accept()
    print("audio connect")
    try:
        while True:
            data = await websocket.receive_json()
            print("audio received")
            disconnected = []
            for browser in connections:
                try:
                    await browser.send_json(data)
                except Exception:
                    print("browser sisconnect")
                    disconnected += [browser]
            for browser in disconnected:
                connections.discard(browser)
    except WebSocketDisconnect:
        print("Disconnected")

@router.websocket("/ws/visual")
async def visualisation(websocket:WebSocket):
    await websocket.accept()
    connections.add(websocket)
    print("brosw connected")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        print("brows disconnected")
        connections.discard(websocket)