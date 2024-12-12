from django import forms
from backend.segment.models import Segment
from .models import Product


class ProductForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Product

        fields = '__all__'

        widgets = {
            'description': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            # 'data_validade': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantidade_un_embalagem': forms.NumberInput(attrs={'min': '0'}),
            'quantidade_embalagem_un_armazenamento': forms.NumberInput(
                attrs={'min': '0'})
        }
