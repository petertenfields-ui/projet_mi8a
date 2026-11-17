import asyncio
import websockets
import json
import math

SERVER_URL = 'ws://127.0.0.1:8000/ws/audio'

async def main():
    async with websockets.connect(SERVER_URL) as websocket:
        print("Connecté fastapi")
        counter = 0
        while True:
            features = {
                "volume":abs(math.sin(counter*0.1)),
                "bass":abs(math.sin(counter*0.2)),
                "mid":abs(math.sin(counter*0.3)),
                "treble":abs(math.sin(counter*0.4))
            }
            await websocket.send(json.dumps(features))
            print("Sent",features)
            counter+=1
            await asyncio.sleep(1)
asyncio.run(main())