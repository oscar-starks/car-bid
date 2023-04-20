import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.channel_name = user_id
        self.room_group_name = user_id
        
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
        
        await self.send(text_data=json.dumps({
            'type':'connection established',
            'message':'connection successful'})
        )
        
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        notification = text_data_json
        
        print(notification)

        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "send_notification", "notification": notification}
        )
    
    async def send_notification(self, event):
        notification = event["notification"]
        await self.send(text_data=json.dumps(notification))
        