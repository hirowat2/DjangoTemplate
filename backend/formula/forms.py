from django import forms
from .models import Formula


class FormulaForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Formula
        fields = '__all__'

        widgets = {
            'a': forms.NumberInput(attrs={'min': '0'}),
            'b': forms.NumberInput(attrs={'min': '0'}),
            'c': forms.NumberInput(attrs={'min': '0'}),

        }
