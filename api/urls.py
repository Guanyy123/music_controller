from django.urls import path

from .views import RoomView, CreateRoomView, GetRoom

urlpatterns = [
    path('room/list', RoomView.as_view()),
    path('room/create', CreateRoomView.as_view()),
    path('room/get',  GetRoom.as_view()),
]