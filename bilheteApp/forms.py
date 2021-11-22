from django import forms
from .models import bilhete
from django.utils.translation import ugettext_lazy as _

class bilhete_form(forms.ModelForm):
    class Meta:
        model = bilhete
        fields = ['mensagem',]
        labels = {
            'mensagem': _('Mensagem'),
        }

    def __init__(self, *args, **kwargs):
        super(bilhete_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'