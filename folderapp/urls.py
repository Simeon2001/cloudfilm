from django.urls import path
from . import views

urlpatterns = [
    path("folder", views.index, name="folder/"),
    path("folder/<str:code>", views.delete_folder, name="folder/"),
]
