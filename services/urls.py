from django.urls import path
from .views import services, service_detail, service_like

app_name = "services"

urlpatterns = [
    path("" , services, name="services"),
    path("category/<str:cat>" , services, name="services_by_category"),
    path("creator/<str:user>" , services, name="services_by_user"),
    path("detail/<int:id>" , service_detail, name="service_detail"),
    path("like/<int:id>" , service_like, name="service_like"),
]