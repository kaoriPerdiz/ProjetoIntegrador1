from django import forms
from .models import controle_saida, pessoas_autorizadas
from django.utils.translation import ugettext_lazy as _
import prototipo.settings as settings

class controle_saida_form(forms.ModelForm):
    data_saida = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = controle_saida
        fields = ['crianca', 'responsavel', 'data_saida',]
        labels = {
            'crianca': _('Aluno'),
            'responsavel': _('Pessoa autorizada') ,
            'data_saida': _('Data da saída'),
        }

    def __init__(self, *args, **kwargs):
        super(controle_saida_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class pessoa_autorizada_form(forms.ModelForm):
    class Meta:
        model = pessoas_autorizadas
        fields = ['crianca', 'nome', 'parentesco', 'telefone']
        labels = {
            'crianca': _('Aluno'),
            'nome': _('Nome') ,
            'parentesco': _('Parentesco'),
            'telefone': _('Telefone') ,
        }

    def __init__(self, *args, **kwargs):
        super(pessoa_autorizada_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'