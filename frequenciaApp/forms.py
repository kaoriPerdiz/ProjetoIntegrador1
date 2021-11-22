from django import forms
from django.forms import fields
from .models import frequencia
from django.utils.translation import ugettext_lazy as _

class frequencia_form(forms.ModelForm):
    class Meta:
        model = frequencia
        fields = ['crianca', 'data_presenca']
        labels = {
            'data_presenca': _('Data da presença'),
        }

    def __init__(self, *args, **kwargs):
        super(frequencia_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'