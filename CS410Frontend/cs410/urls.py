from django.urls import path
from cs410 import views

urlpatterns = [
    path("main/", views.main, name="main"),
    path('search/',views.search, name='search'),
]