from django.urls import path
from pages import views

urlpatterns = [
    path("ask/", views.ask, name="ask")
]
