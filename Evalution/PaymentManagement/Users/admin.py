from django.contrib import admin
from .models import ServiceUser, Service, Subscription
# Register your models here.


admin.site.register(ServiceUser)
admin.site.register(Service)
admin.site.register(Subscription)

