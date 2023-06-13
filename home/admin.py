from django.contrib import admin
from .models import contact,act
# Register your models here.

class contactadmin(admin.ModelAdmin):
	list_display=('name','email','sub','message')

class actadmin(admin.ModelAdmin):
	list_display=('name32','email32','sub32','message32')

admin.site.register(contact,contactadmin)
admin.site.register(act,actadmin)
