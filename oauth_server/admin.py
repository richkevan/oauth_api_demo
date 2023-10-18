from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Response_types)
admin.site.register(models.Scope)
admin.site.register(models.Grant_types)