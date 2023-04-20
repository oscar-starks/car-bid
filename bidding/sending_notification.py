import json, asyncio, websockets

async def send_message():
    uri = "ws://localhost:8000/socketserver/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"message":"the message works"}))

asyncio.run(send_message())
