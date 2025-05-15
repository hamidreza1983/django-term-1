from django.shortcuts import render, get_object_or_404
from .models import Services, Specials



# Create your views here.

def services(request, cat=None):
    #category = request.GET.get("category")
    if cat:
        services = Services.objects.filter(category__name=cat, status=True)
    else:
        services = Services.objects.filter(status=True)
    specials = Specials.objects.filter(status=True)
    context = {
        "services" : services,
        "specials" : specials,
    }
    return render(request, "services/services.html", context=context)


def service_detail(request, id):
    try:
        service = Services.objects.get(pk=id)
        context = {
            "service" : service
        }
        return render(request, "services/service-details.html", context=context)
    except:
        return render(request, "home/404.html", status=404)
    
def service_null(request):
    return services(request)


    
    

# Create your views here.
