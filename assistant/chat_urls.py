from assistant import views
from django.urls import path

urlpatterns = [
    path('', views.chat, name="Assistant"),
    
]