from django import forms

from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProductForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Product
        # fields = ('title', 'description', 'category')
        fields = '__all__'

        # fields = [
        #     'title', 'description', 'price', 'category',
        #     'un_estoque', 'tipo_embalagem',
        #     'slug', 'planta',
        #     'codigo', 'novo_codigo', 'data_validade', 'quantidade_un_embalagem',
        #     'quantidade_embalagem_un_armazenamento', 'codigo_predecessor', 'segmentation'
        # ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'data_validade': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantidade_un_embalagem': forms.NumberInput(attrs={'min': '0'}),
            'quantidade_embalagem_un_armazenamento': forms.NumberInput(attrs={'min': '0'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'