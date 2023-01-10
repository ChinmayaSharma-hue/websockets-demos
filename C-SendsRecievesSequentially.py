import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:8000") as websocket:
        numbering = 0
        while True:
            sending_message = "Hey Server!"
            await websocket.send(sending_message)
            await asyncio.sleep(2)

            message = await websocket.recv()
            print(f"{numbering}. Received message: {message}")
            numbering += 1

asyncio.run(hello())
