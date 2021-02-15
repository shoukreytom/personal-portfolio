from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/<slug:slug>/', views.portfolio_details, name='portfolio-details'),
    path('feedback/send_mail/', views.send_email, name='send-email'),
    path('visit/cv/', views.visit_cv, name='visit-cv'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)