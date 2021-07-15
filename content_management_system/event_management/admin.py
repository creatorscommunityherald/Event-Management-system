from django.contrib import admin

from .models import Competition,Event,Registration,Competition_Registration,Look_and_feel

# Register your models here.
admin.site.register(Competition_Registration)
admin.site.register(Registration)
admin.site.register(Competition)
admin.site.register(Event)
admin.site.register(Look_and_feel)