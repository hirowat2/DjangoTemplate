from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Product
        # fields = ('title', 'description', 'category')
        fields = [
            'title', 'description', 'price', 'category',
            'un_estoque', 'tipo_embalagem',
            'slug', 'planta',
            'codigo', 'novo_codigo', 'data_validade', 'quantidade_un_embalagem',
            'quantidade_embalagem_un_armazenamento', 'codigo_predecessor', 'segmentation'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'data_validade': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantidade_un_embalagem': forms.NumberInput(attrs={'min': '0'}),
            'quantidade_embalagem_un_armazenamento': forms.NumberInput(attrs={'min': '0'})
        }
