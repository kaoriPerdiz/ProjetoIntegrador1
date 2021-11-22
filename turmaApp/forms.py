from django import forms
from .models import turma
from django.utils.translation import ugettext_lazy as _

class turma_form(forms.ModelForm):
    class Meta:
        model = turma
        fields = ['nome_turma', 'serie', 'nome_professor_monitor',]
        labels = {
            'nome_turma': _('Nome da turma'),
            'serie': _('Série') ,
            'nome_professor_monitor': _('Nome do(a) professor(a)/monitor(a)'),
        }

    def __init__(self, *args, **kwargs):
        super(turma_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'