from django.contrib import admin

# Register your models here.

from . import models


class KinologAdmin(admin.ModelAdmin):
    list_display=('pk','name')
    list_editable=('name',)

    

admin.site.register(models.Kinolog, KinologAdmin)
