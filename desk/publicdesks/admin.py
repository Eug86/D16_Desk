from django.contrib import admin
from .models import Ann


@admin.register(Ann)
class AnnAdmin(admin.ModelAdmin):
    model = Ann
