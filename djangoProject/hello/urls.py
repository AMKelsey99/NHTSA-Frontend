from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="hello"),
    path('services', views.services, name="services"),
    path('faq', views.faq, name="faq"),
    path('contact', views.contact, name="contact"),
    path('register', views.register, name="register"),
    path('login_page', views.login_page, name="login_page"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('appt', views.appointments, name="appointments"),
]