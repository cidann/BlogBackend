from django.contrib import admin
from content.models import Blog

# Register your models here.
class DefaultAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog,DefaultAdmin)