import json, websockets
from knox.models import AuthToken
from accounts.models import User
from asgiref.sync import sync_to_async
from websockets.sync.client import connect

async def send_message(notification:str):
    uri = "ws://localhost:8000/general_notifications/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"message": notification}))

async def bid_message(offer:str, car_id:str, offer_id:str):
    uri = "ws://localhost:8000/offers/" + car_id + "/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"offer": offer, "offer_id":offer_id}))

# def personal_notifcations(user_id:str, message:str):
#     user = User.objects.get(id = user_id)
#     token = AuthToken.objects.create(user=user)
#     token = token[1]
#     print(token)
#     url = f"ws://localhost:8000/notifications/{user_id}/" + f"?token=" + str(token)

#     with connect(url) as websocket:
#         websocket.send(json.dumps({"message": message}))
