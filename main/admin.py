from django.contrib import admin
from .models import Member, Agency, Campaign

# Register your models here.
admin.site.register(Member)
admin.site.register(Agency)
admin.site.register(Campaign)