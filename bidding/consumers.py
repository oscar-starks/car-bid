import json
from channels.generic.websocket import AsyncWebsocketConsumer

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
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "offer", "offer": offer["offer"]}
        )
       
    async def offer(self, event):
        await self.send(text_data=json.dumps(event))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)