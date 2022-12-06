from django.contrib import admin

from .models import Packages,Orders,contact

admin.site.register(Packages)
admin.site.register(Orders)
admin.site.register(contact)