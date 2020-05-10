from django.urls import path
from .views import websocket_example

urlpatterns = [
    path('websocket/', websocket_example, name="websocket_example"),
]