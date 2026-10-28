from django.contrib import admin

from .models import CustomerProfile, VendorEmployee


admin.site.register(CustomerProfile)
admin.site.register(VendorEmployee)
