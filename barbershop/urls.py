from django.urls import path
from barbershop import views

# Urls de la aplicación facturación

urlpatterns = [
    # Inicio
    path("", views.index, name="index"),
    path('home/', views.home, name='home'),

]
