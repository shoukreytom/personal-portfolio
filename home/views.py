from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse, Http404, FileResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

from .models import Portfolio


def home(request):
    portfolios = Portfolio.objects.all()
    ctx = {
        'portfolios': portfolios,
    }
    return render(request, "home/index.html", ctx)

def portfolio_details(request, slug):
    try:
        portfolio = Portfolio.objects.get(slug=slug)
    except Portfolio.DoesNotExist:
        return Http404("This portfolio is not found")
    ctx = {
        'portfolio': portfolio,
    }
    return render(request, "home/portfolio-details.html", ctx)

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        message = name + "\n" + email + "\n" + message
        send_mail(subject, message, email, [settings.EMAIL_HOST_USER])
        messages.success(request, "The message has been sent successfully")
        return redirect(reverse('home'))
    else:
        return HttpResponse("<h1>bad request</h1>")

def visit_cv(request):
    book_url = "https://drive.google.com/file/d/19ej-R9QEhWGNOwNjTaZ10-ddfWKjQ5mo/view?usp=sharing"
    return redirect(book_url)

def error404(request, exception=None):
    return render(request, 'home/404.html')

def error500(request):
    return render(request, 'home/500.html')
