import json
from channels.generic.websocket import AsyncWebsocketConsumer
from accounts.models import User



class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "general_notifications"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name)

        await self.accept()
        
        await self.send(text_data=json.dumps({
            'type':'connection established',
            'message':'connection successful'})
        )
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        notification = text_data_json
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "notification", "notification": notification["message"]}
        )
       
    async def notification(self, event):
        await self.send(text_data=json.dumps(event))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


class CarOfferConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        car_id = self.scope["url_route"]["kwargs"]["car_id"]
        print(car_id)
        self.room_group_name = car_id
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name)

        await self.accept()
        
        await self.send(text_data=json.dumps({
            'type':'connection established',
            'message':'connection successful'})
        )
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        offer = text_data_json
        print(offer)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "offer", "offer": offer["offer"], "offer_id": offer["offer_id"]}
        )
       
    async def offer(self, event):
        await self.send(text_data=json.dumps(event))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


class PersonalNotificationsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]
        user_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.room_group_name = user_id

        try:
            if str(user.id) == user_id:
                await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name)

                await self.accept()
                
                await self.send(text_data=json.dumps({
                    'type':'connection established',
                    'message':'connection successful'})
                )
        except:
            pass
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "notification", "message": message["message"]}
        )
       
    async def notification(self, event):
        await self.send(text_data=json.dumps(event))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]
        chat_id = self.scope["url_route"]["kwargs"]["chat_id"]

        self.room_group_name = chat_id
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        print(message)

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps(message))
