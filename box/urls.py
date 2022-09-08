from django.urls import path
from . import views

urlpatterns = [
    path ('store/<str:code>', views.upload_file, name = 'file/' ),
]