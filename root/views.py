from django.shortcuts import render
from .models import Pricing, Leader

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    leaders = Leader.objects.filter(status=True)
    context={
        "leaders" : leaders,
        }
    return render(request, "home/about.html", context=context)


def pricing(request):
    return render(request, "home/pricing.html")