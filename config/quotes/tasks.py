import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer


channel_layer = get_channel_layer()


@shared_task
def get_quote():
    url = 'https://api.quotable.io/quotes/random'
    response = requests.get(url).json()
    quote = {
        'content': response['content'],
        'author': response['author'],
        'tags': response['tags'][0] if response['tags'] else 'No Tag',
    }
    print(quote)
    async_to_sync(channel_layer.group_send)(
        'quotes',
        {
            'type': 'send_quotes',
            'text': quote
        }
    )
