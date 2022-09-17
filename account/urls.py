from django.urls import path
from . import views

urlpatterns = [
    path("token", views.authr_token),
    path("signup", views.usercreateview),
]
