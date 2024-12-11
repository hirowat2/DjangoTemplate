from django import forms
from .models import Segment


class SegmentForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Segment
        fields = '__all__'

        widgets = {
            'description': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'possible_segment': forms.Textarea(attrs={'rows': 1, 'cols': 30})
        }


