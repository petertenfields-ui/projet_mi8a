import asyncio
import json
import websockets
#from audio.analyse import analyse_audio
from audio.capture import open_microphone
#TODO : combiner analyse et audio pour envoyer le JSON
SAMPLE_RATE = 44100
BLOCK_SIZE = 2080
SERVER_URL = "ws://l'adresse_ip"
async def main():
    with open_microphone(SAMPLE_RATE, BLOCK_SIZE) as microphone:
        #connection au serveur FastAPI
        pass
        """
        async with websockets.connect(uri = SERVER_URL) as websocket:
            while True:
                samples, overflowed = await asyncio.to_thread(
                            microphone.read,
                            BLOCK_SIZE
                            )
                #assuming the output of the audio analysis is gonna be of the form {'frequency':int, 'treble':int}
                features = analyse_audio(samples[:,0], SAMPLE_RATE)
                await websocket(json.dump(features))
        """
if __name__ == '__main__':
    asyncio.run(main())