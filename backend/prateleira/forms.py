from django import forms

from .models import Prateleira


class PrateleiraForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Prateleira
        # fields = ('title', 'description', 'category')
        fields = [
            'product',
            'planta',
            'codigo',
            'descricao',
            'formula_calculo',
            'reserva_historico',
            'inicio_reserva',
            'fim_reserva',
            'reserva',
            'segurança',
            'pulmao',
            'ciclo',
            'dep_maximo',
            'dep_medio',
            'quarentena',
            'transito',
            'prateleira_total',
            'pto_reposicao',
            'slug'
        ]
        widgets = {
            'planta': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'codigo': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'descricao': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'formula_calculo': forms.NumberInput(attrs={'min': '0'}),
            'reserva_historico': forms.NumberInput(attrs={'min': '0'}),
            'inicio_reserva': forms.NumberInput(attrs={'min': '0'}),
            'fim_reserva': forms.NumberInput(attrs={'min': '0'}),
            'reserva': forms.NumberInput(attrs={'min': '0'}),
            'segurança': forms.NumberInput(attrs={'min': '0'}),
            'pulmao': forms.NumberInput(attrs={'min': '0'}),
            'ciclo': forms.NumberInput(attrs={'min': '0'}),
            'dep_maximo': forms.NumberInput(attrs={'min': '0'}),
            'dep_medio': forms.NumberInput(attrs={'min': '0'}),
            'quarentena': forms.NumberInput(attrs={'min': '0'}),
            'transito': forms.NumberInput(attrs={'min': '0'}),
            'prateleira_total': forms.NumberInput(attrs={'min': '0'}),
            'pto_reposicao': forms.NumberInput(attrs={'min': '0'}),
            'slug': forms.NumberInput(attrs={'min': '0'})

        }
