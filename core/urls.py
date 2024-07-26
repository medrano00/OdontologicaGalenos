from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # - - - - - - - - - - URLs vitales de la página - - - - - - - - - - #
    path('', home, name='home'),
    path('reservaRealizada/', reservaRealizada, name='reservaRealizada'),
    # - - - - - - - - - - Sección de Administración de Vistas de Cuentas de Usuario - - - - - - - - - - #
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # - - - - - - - - - - Sección de Mantención de sistema CRUD (Create, Read, Update & Delete) - - - - - - - - - - #
    path('reservarCita/', reservarCita, name='reservarCita'),
    path('admin/', admin, name='admin'),
    path('reserva_edit/<str:pk>/', editar_reserva, name='reserva_edit'),
    path('reserva_del/<str:pk>', reserva_del, name='reserva_del'),
    # - - - - - - - - - - Método de Recuperación de Contraseña por Portal de Django - - - - - - - - - - #
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]