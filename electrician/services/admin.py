from django.contrib import admin
from .models import Services

# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("title", 'price', 'created_at', 'updated_at')
    fields = ('title', 'price', 'updated_at',)
    search_fields = ("title", )
    readonly_fields = ("created_at", "updated_at")
    ordering = ("title", )
