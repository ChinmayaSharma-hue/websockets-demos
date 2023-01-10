import asyncio
import websockets


async def hello(websocket, path):
    while True:
        await websocket.send(f"Hello client!")
        await asyncio.sleep(1)


async def main():
    async with websockets.serve(hello, "localhost", 8000):
        await asyncio.Future()

asyncio.run(main())
