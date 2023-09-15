from django.contrib import admin
from .models import Proposal

class PropostaAdmin(admin.ModelAdmin):
    list_display = ('document', 'name', 'approved')  # Campos exibidos na lista de propostas
    list_editable = ('approved',)  # Campos editáveis diretamente na lista

admin.site.register(Proposal, PropostaAdmin)
