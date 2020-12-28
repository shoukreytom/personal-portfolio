from django.shortcuts import render


def home(request):
    return render(request, "home/index.html")

def portfolio_details(request, pk):
    return render(request, "home/portfolio-details.html")
