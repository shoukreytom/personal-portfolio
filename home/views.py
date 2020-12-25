from django.shortcuts import render


def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def resume(request):
    return render(request, "home/resume.html")

def portfolio(request):
    return render(request, "home/portfolio.html")

def contact(request):
    return render(request, "home/contact.html")

def portfolio_details(request, pk):
    return render(request, "home/portfolio-details.html")
