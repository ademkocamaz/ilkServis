from django.contrib import admin
from baton.models import BatonTheme

# Register your models here.
from service._admin.service import ServiceAdmin

admin.site.unregister(BatonTheme)