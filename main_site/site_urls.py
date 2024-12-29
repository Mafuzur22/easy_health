from unicodedata import name
from main_site import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="Home"),
    path('login', views.login_view, name="Login"),
    path('register', views.register_view, name="Login"),
    path("logout", views.logout_view, name="Logout")
    
]