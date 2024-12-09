from django.urls import path
from .views import bot_handler
from django.http import HttpResponseNotFound

urlpatterns = [
    path('favicon.ico', lambda request: HttpResponseNotFound()),

    path('bot-endpoint/', bot_handler),
]
