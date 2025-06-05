from django.shortcuts import render,redirect
from .models import Pricing, Leader, ContactUs
from services.models import Services
from django.contrib import messages
from .forms import ContactUsForm

# Create your views here.

def home(request):
    services = Services.objects.all().order_by("-counted_view")[:3]
    context={
        "services" : services,
        }
    return render(request, "home/index.html", context=context)

def contact(request):
    if request.method == "GET":
        form = ContactUsForm()
        return render(request, "home/contact.html", context={"form" : form})
    elif request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "your contact received successfully...")
            return render(request, "home/contact.html")
        else:
            messages.add_message(request, messages.ERROR, "your input data is not valid")
            return redirect("root:contact")

        
    

def about(request):
    leaders = Leader.objects.filter(status=True)
    context={
        "leaders" : leaders,
        }
    return render(request, "home/about.html", context=context)


def pricing(request):
    return render(request, "home/pricing.html")