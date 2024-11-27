from django.urls import path
from .views import hello_view, confirmation_view

urlpatterns = [
    path('hello/<str:name>/', hello_view),
    path('confirmation/', confirmation_view),
]