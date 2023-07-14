from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "cost",
        "date",
        "from_day"
    ]


admin.site.register(Order, OrderAdmin)
