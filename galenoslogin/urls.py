from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('indexwithlogin', views.indexwithlogin, name='indexwithlogin'),
    path('registration/', LoginView.as_view(), name='login'),
    path('', LogoutView.as_view(), name='logout'),
    path('reservarCita/', views.reservarCita, name='reservarCitaLogin'),
]