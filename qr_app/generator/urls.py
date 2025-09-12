from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_qr, name='generate_qr'),
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
    path('confirm-payment/', views.confirm_payment, name='confirm_payment'),
    path('download/<uuid:qr_id>/', views.download_hd, name='download_hd'),
]