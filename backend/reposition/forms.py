from django import forms

from .models import Reposition


class RepositionForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Reposition
        fields = [
            'lt_pre_ordem',
            'lt_ordem',
            'lt_quarentena',
            'lt_total',
            'cv_lead_time',
            'lote_minimo_rep',
            'lote_multiplo_rep',
            'intervalo_reposicao',
            'campanha_ideal',
            'slug'
        ]
        widgets = {
            'lt_pre_ordem': forms.NumberInput(attrs={'class': 'form-control'}),
            'lt_ordem': forms.NumberInput(attrs={'class': 'form-control'}),
            'lt_quarentena': forms.NumberInput(attrs={'class': 'form-control'}),
            'lt_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'cv_lead_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'lote_minimo_rep': forms.NumberInput(attrs={'class': 'form-control'}),
            'lote_multiplo_rep': forms.NumberInput(attrs={'class': 'form-control'}),
            'intervalo_reposicao': forms.NumberInput(attrs={'class': 'form-control'}),
            'campanha_ideal': forms.NumberInput(attrs={'class': 'form-control'})
        }
