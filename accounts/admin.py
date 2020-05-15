from django.contrib import admin
from .models import Customer, Product, Order, Tag


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_created')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
