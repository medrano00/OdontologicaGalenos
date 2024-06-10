from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('indexwithlogin', views.indexwithlogin, name='indexwithlogin'),
    path('registration/', LoginView.as_view(), name='login'),
    path('', LogoutView.as_view(), name='logout'),
    path('reservarCita/', views.reservarCita, name='reservarCitaLogin'),
    path('reservaRealizada/', views.reservaRealizada, name='reservaRealizada'),
    path('admin/', views.admin, name='admin'),
    path('reserva_del/<str:pk>', views.reserva_del, name='reserva_del'),
    path('reserva_edit/<str:pk>/', views.editar_reserva, name='reserva_edit'),
    path('registration/', LoginView.as_view(), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# Include static file handlers for testing
urlpatterns += staticfiles_urlpatterns()