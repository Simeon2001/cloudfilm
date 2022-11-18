from django.urls import path
from box import views
from box import baseview

urlpatterns = [
    path("store/<str:code>", views.upload_file, name="file/"),
    path("basestore/<str:code>", baseview.upload_basefile, name="basefile/"),
    path("store/<str:code>/del/<str:idd>", views.delete_file, name="delete_file/"),
    path("metrics", views.storage_metrics, name="metrics/"),
]
