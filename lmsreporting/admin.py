from django.contrib import admin
from .models import Issue, Module

# Register your models here.
admin.site.register(Module)
admin.site.register(Issue)
