from django.urls import path
from cs410 import views

urlpatterns = [
    path("main/", views.main, name="main"),
    path('search/',views.search, name='search'),
    path('entryview/<int:id>',views.entryview, name="entryview"),
    path('register', views.register, name="register"),
    path('login_page', views.login_page, name="login_page"),
    path('logout_view', views.logout_view, name="logout_view"),
]