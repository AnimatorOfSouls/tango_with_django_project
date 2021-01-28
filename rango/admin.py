from django.contrib import admin
from rango.models import Category, Page     #add name of model when adding new model

#add new register when adding new model
admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    list_display = ("title","category","url")
admin.site.register(Page, PageAdmin)
