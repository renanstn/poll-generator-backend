from django.urls import path
from core.websocket import consumers


websocket_urlpatterns = [
    path("ws/", consumers.Consumer.as_asgi()),
]
