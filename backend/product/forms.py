from django import forms
from backend.segment.models import Segment
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Obtendo todos os segmentos
        segmentos = Segment.objects.all()

        # Adicionando campos dinamicamente
        for segmento in segmentos:
            field_name = segmento.title.replace(" ", "_").lower()  # Nome do campo baseado no título
            choices = [(opt, opt) for opt in segmento.possible_segment.split(",")]  # Dividindo os valores por vírgula

            # Criando o campo no formulário
            self.fields[field_name] = forms.ChoiceField(
                choices=choices,
                label=segmento.title,
                required=False
            )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            # 'data_validade': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantidade_un_embalagem': forms.NumberInput(attrs={'min': '0'}),
            'quantidade_embalagem_un_armazenamento': forms.NumberInput(
                attrs={'min': '0'})
        }
