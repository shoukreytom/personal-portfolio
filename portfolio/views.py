from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from portfolio.models import Portfolio, Screenshot
from portfolio.serializers import PortfolioSerializer, ScreenshotSerializer


class PortfolioList(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioDetails(RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ScreenshotList(APIView):
    def get(self, request, pk):
        portfolio = get_object_or_404(Portfolio, pk=pk)
        print(portfolio)
        screenshots = Screenshot.objects.filter(portfolio=portfolio)
        serializer = ScreenshotSerializer(screenshots, many=True)
        return Response(serializer.data)


class SendEmail(APIView):
    def post(self, request):
        data = dict()
        STATUS_CODE = 200
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            message = name + "\n" + email + "\n" + message
            send_mail(subject, message, email, [settings.EMAIL_HOST_USER], fail_silently=False)
            msg = "an email has been sent successfully."
        except:
            STATUS_CODE = 400
            msg = "failed to sent an email, please! try again."
        data["message"] = msg
        data["status"] = STATUS_CODE
        return Response(data, status=STATUS_CODE)

