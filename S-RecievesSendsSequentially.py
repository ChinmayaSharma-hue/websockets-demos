import asyncio
import websockets


async def hello(websocket, path):
    numbering = 0
    while True:
        recieved_message = await websocket.recv()
        print(f"{numbering}. Received message: {recieved_message}")
        numbering += 1

        await websocket.send(f"Hello client!")
        await asyncio.sleep(2)


async def main():
    async with websockets.serve(hello, "localhost", 8000):
        await asyncio.Future()

asyncio.run(main())
