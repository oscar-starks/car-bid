import json, asyncio, websockets

async def send_message(notification:str):
    uri = "ws://localhost:8000/general_notifications/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"message": notification}))

# async def bid_message():
#     uri = "ws://localhost:8000/general_notifications/"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send(json.dumps())
