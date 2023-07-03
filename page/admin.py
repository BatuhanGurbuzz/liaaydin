from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Contact, Products, OurServices

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'mail')

    search_fields = ('name', 'mail')
    readonly_fields = ('name', 'subject', 'mail', 'message')
    
    
    fields = ('name', 'subject', 'mail', 'message')

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)

class OurServicesAdmin(admin.ModelAdmin):
    list_display = ("comment",)
    search_fields = ('comment',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(OurServices, OurServicesAdmin)