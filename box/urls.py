from django.urls import path
from . import views

urlpatterns = [
    path("store/<str:code>", views.upload_file, name="file/"),
    path("store/<str:code>/del/<str:idd>", views.delete_file, name="delete_file/"),
    path("metrics", views.storage_metrics, name="metrics/"),
]
