from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    ordering = ('title',)

admin.site.register(Page, PageAdmin)
