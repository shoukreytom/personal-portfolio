from django.urls import path
from portfolio import views


urlpatterns = [
    path("", views.PortfolioList.as_view()),
    path("<int:pk>/", views.PortfolioDetails.as_view()),
    path("<int:pk>/screenshots/", views.ScreenshotList.as_view()),
    path("email/", views.SendEmail.as_view()),
]
