from django.shortcuts import render


def home(request):
    return render(request, "home/index.html")

def portfolio_details(request, pk):
    return render(request, "home/portfolio-details.html")


def error404(request, exception=None):
    return render(request, 'home/404.html')

def error500(request):
    return render(request, 'home/500.html')
