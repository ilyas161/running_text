from django.urls import path

from . import views

urlpatterns = [
    path("video", views.textrun, name="video"),
    path("texts", views.listOfText, name="texts"),
]