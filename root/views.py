from django.shortcuts import render
from .models import Pricing, FrequnlyQuestion

# Create your views here.

def home(request):
    pricings = Pricing.objects.filter(status=True).order_by("-created_at")
    questions = FrequnlyQuestion.objects.filter(status=True)
    context={
        "pricing" : pricings,
        "questions" : questions
        }
    return render(request, "home/index.html", context=context)

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")


def pricing(request):
    return render(request, "home/pricing.html")