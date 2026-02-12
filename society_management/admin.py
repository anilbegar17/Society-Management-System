from django.contrib import admin

# Register your models here.
from .models import User, Society, Flat, MaintenanceBill

admin.site.register(User)
admin.site.register(Society)
admin.site.register(Flat)
admin.site.register(MaintenanceBill)
