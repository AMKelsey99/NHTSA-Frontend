from django.urls import path
from cs410 import views

urlpatterns = [
    path('', views.main, name="main"),
    path('search/', views.search, name='search'),
    path('entryview/<int:vehicle_id>/',views.entryview, name="entryview"),
    path('register/', views.register, name="register"),
    path('accounts/login/', views.login_page, name="login_page"),
    path('accounts/logout', views.logout_view, name="logout_view"),
    path('adminview/', views.adminview, name="adminview"),
    path('adminview/accounts/login/', views.login_page, name="login_page"),
    path('history/', views.history, name="history"),
    path('history/accounts/login/', views.login_page, name="login_page"),
    path('afield1/', views.afield1, name="afield1"),
    path('afield2/', views.afield2, name="afield2"),
    path('afield3/', views.afield3, name="afield3"),
    path('dfield1/', views.dfield1, name="dfield1"),
    path('dfield2/', views.dfield2, name="dfield2"),
    path('dfield3/', views.dfield3, name="dfield3"),
    path('delete/<int:vehicle_id>/',views.delete, name="delete"),
]
