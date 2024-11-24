from django import forms

from .models import Consume


class ConsumeForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Consume
        # fields = ('title', 'description', 'category')
        fields = [
            'consumo_historico',
            'cv_diario',
            'cv_periodo_lt',
            'demanda_dia_prev',
            'fator_k',
            'slug'
        ]
        widgets = {
            'consumo_historico': forms.NumberInput(attrs={'min': '0'}),
            'cv_diario': forms.NumberInput(attrs={'min': '0'}),
            'cv_periodo_lt': forms.NumberInput(attrs={'min': '0'}),
            'demanda_dia_prev': forms.NumberInput(attrs={'min': '0'}),
            'fator_k': forms.NumberInput(attrs={'min': '0'})

        }
