from django.urls import path
from . import views

urlpatterns = [
    path ('folder', views.index, name = 'cart/' ),
    path ('store/<str:code>', views.upload_file, name = 'cart/' ),
]