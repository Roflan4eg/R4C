from django.urls import path
from . import views

urlpatterns = [
    path('download_report/', views.download_report),
]
