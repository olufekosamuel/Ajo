from django.contrib import admin
from django.urls import path, include
from .views import UserListView, LoginView, LogoutView

urlpatterns = [
    path('', UserListView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
]
