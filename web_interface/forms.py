from django import forms
from .models import Proposal

class ProposalForm(forms.Form):
    document = forms.CharField(label="Documento", max_length=100)
    name = forms.CharField(label="Nome", max_length=100)