from django.urls import path
from . import views

urlpatterns = [
    path("<int:page_id>/", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("mylists/", views.mylists, name="mylists"),
    path("applicable_<int:list_id>/", views.applicable, name="applicable"),
]