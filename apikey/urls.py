from django.urls import path
from . import views

urlpatterns = [
    path("key", views.get_apikey),
]