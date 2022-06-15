from django.contrib import admin
from .models import testModel

# Register your models here.

class testModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(testModel, testModelAdmin)