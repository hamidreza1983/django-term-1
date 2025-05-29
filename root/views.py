from django.shortcuts import render
from .models import Pricing, Leader, ContactUs
from services.models import Services
from django.contrib import messages

# Create your views here.

def home(request):
    services = Services.objects.all().order_by("-counted_view")[:3]
    context={
        "services" : services,
        }
    return render(request, "home/index.html", context=context)

def contact(request):
    if request.method == "GET":
        return render(request, "home/contact.html")
    elif request.method == "POST":
        if request.POST.get("name"):
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            new_contact = ContactUs()
            new_contact.name = name
            new_contact.email = email
            new_contact.subject = subject
            new_contact.message = message
            new_contact.save()
            messages.add_message(request, messages.SUCCESS, "your contact received successfully...")
            return render(request, "home/contact.html")
        
    

def about(request):
    leaders = Leader.objects.filter(status=True)
    context={
        "leaders" : leaders,
        }
    return render(request, "home/about.html", context=context)


def pricing(request):
    return render(request, "home/pricing.html")