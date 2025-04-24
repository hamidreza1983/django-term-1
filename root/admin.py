from django.contrib import admin
from .models import Pricing, Items, FrequnlyQuestion



admin.site.register(Items)
admin.site.register(FrequnlyQuestion)

# Register your models here.


class CustomePricing(admin.ModelAdmin):
    list_display = ["title", "amount", "status"]
    list_filter = ["status"]
    search_fields = ["title"]


admin.site.register(Pricing, CustomePricing)