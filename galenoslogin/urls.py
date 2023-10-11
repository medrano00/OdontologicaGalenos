from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('indexwithlogin', views.indexwithlogin, name='indexwithlogin'),
    path('registration/', LoginView.as_view(), name='login'),
    path('', LogoutView.as_view(), name='logout'),
    path('reservarCita/', views.reservarCita, name='reservarCitaLogin'),
    path('reservaRealizada/', views.reservaRealizada, name='reservaRealizada'),
]

# Include static file handlers for testing
urlpatterns += staticfiles_urlpatterns()