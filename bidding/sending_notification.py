import json, asyncio, websockets

async def send_message():
    uri = "ws://localhost:8000/ws/socket-server/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"type":"chat","message":"hello suckersss"}))

asyncio.run(send_message())
