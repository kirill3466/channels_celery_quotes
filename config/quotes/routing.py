from django.urls import path

from quotes.consumers import QuotesConsumer

ws_urlpatterns = [
    path('ws/quotes/', QuotesConsumer.as_asgi()),
]
