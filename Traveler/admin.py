from django.contrib import admin

from .models import Packages,Orders,contact, RazorpayKeys

admin.site.register(Packages)
admin.site.register(Orders)
admin.site.register(contact)

admin.site.register(RazorpayKeys)