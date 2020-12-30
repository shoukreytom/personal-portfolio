from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/<int:pk>/', views.portfolio_details, name='portfolio-details'),
    path('feedback/send_mail/', views.send_email, name='send-email'),
]