from django.urls import path
from .views import AddRobot

urlpatterns = [
    path('add-robot/', AddRobot.as_view()),
]