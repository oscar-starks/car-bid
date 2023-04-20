import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SampleConsumer(AsyncWebsocketConsumer):
    async def talk_to_worker(self, url, message):
        async with websockets.connect(url) as worker_ws:
            await worker_ws.send(json.dumps(message))
            result = json.loads(await worker_ws.recv())
        await self.send(text_data=json.dumps({ 'to': 'Client' })
