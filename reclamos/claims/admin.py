from django.contrib import admin
from .models import Claim

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'tipo_documento', 'numero_documento', 'tipo_reclamacion', 'status', 'created_at')
    list_filter = ('tipo_reclamacion', 'status', 'created_at')
    search_fields = ('nombre', 'apellido', 'numero_documento', 'email')
    ordering = ('-created_at',)