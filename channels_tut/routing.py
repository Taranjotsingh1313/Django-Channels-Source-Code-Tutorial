from django.urls import path
from channels.routing import URLRouter
from chat.consumers import ChatConsumer
ws_application = [
    path("ws/chat/",ChatConsumer.as_asgi())
]