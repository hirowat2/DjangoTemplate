from django import forms

from .models import Consume


class ConsumeForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Consume
        # fields = ('title', 'description', 'category')
        fields = [
            'product',
            'planta',
            'codigo',
            'descricao',
            'consumo_historico',
            'cv_diario',
            'cv_periodo_lt',
            'demanda_dia_prev',
            'fator_k',
            'menor_lote_consumo',
            'slug'
        ]
        widgets = {
            'planta': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'codigo': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'descricao': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'consumo_historico': forms.NumberInput(attrs={'min': '0'}),
            'cv_diario': forms.NumberInput(attrs={'min': '0'}),
            'cv_periodo_lt': forms.NumberInput(attrs={'min': '0'}),
            'demanda_dia_prev': forms.NumberInput(attrs={'min': '0'}),
            'fator_k': forms.NumberInput(attrs={'min': '0'}),
            'menor_lote_consumo': forms.NumberInput(attrs={'min': '0'}),
            'slug': forms.NumberInput(attrs={'min': '0'})

        }
