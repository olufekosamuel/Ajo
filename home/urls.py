from django.contrib import admin
from django.urls import path, include
from .views import GroupListView,GroupMemberListView,IdGeneratorView, IdAccept

urlpatterns = [
    path('', GroupListView.as_view()),
    path('<int:id>/members', GroupMemberListView.as_view()),
    path('generate', IdGeneratorView.as_view()),
    path('accept/<str:id>', IdAccept, name='Idaccept' ),
]
