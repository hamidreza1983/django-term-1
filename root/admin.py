from django.contrib import admin
from .models import Pricing, Items, FrequnlyQuestion, Team, Skills, Star, Leader, ContactUs



admin.site.register(Items)
admin.site.register(FrequnlyQuestion)
admin.site.register(Team)
admin.site.register(Skills)
admin.site.register(Leader)
admin.site.register(ContactUs)

# Register your models here.


class CustomePricing(admin.ModelAdmin):
    list_display = ["title", "amount", "status"]
    list_filter = ["status"]
    search_fields = ["title"]


admin.site.register(Pricing, CustomePricing)