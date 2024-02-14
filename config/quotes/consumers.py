import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class QuotesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("Connected!")
        await self.channel_layer.group_add('quotes', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        logger.info("Disconnected!")
        await self.channel_layer.group_discard('quotes', self.channel_name)

    async def send_quotes(self, event):
        logger.info(f"sending quote: {event}")
        message = event['text']
        await self.send(json.dumps(message))
