from django import forms
from .models import matricula
from django.utils.translation import ugettext_lazy as _

class matricula_form(forms.ModelForm):
    class Meta:
        model = matricula
        fields = ['nome_crianca', 'data_nascimento_crianca', 'nome_mae', 'telefone_mae', 'servico_mae', 'telefone_servico_mae', 'nome_pai', 'telefone_pai', 'servico_pai', 'telefone_servico_pai', 'cuidado_medico_observacao', 'cuidado_medico_plano_saude', 'logradouro', 'bairro', 'turma']
        labels = {
            'nome_crianca': _('Nome da criança'),
            'data_nascimento_crianca': _('Data de nascimento da criança') ,
            'nome_mae': _('Nome da mãe/responsável'),
            'telefone_mae': _('Telefone da mãe/responsável'),
            'servico_mae': _('Serviço da mãe/responsável'),
            'telefone_servico_mae': _('Telefone do serviço da mãe/responsável'),
            'nome_pai': _('Nome do pai/responsável'),
            'telefone_pai': _('Telefone do pai/responsável'),
            'servico_pai': _('Serviço do pai/responsável'),
            'telefone_servico_pai': _('Telefone do serviço do pai/responsável'),
            'cuidado_medico_observacao': _('Observação'),
            'cuidado_medico_plano_saude': _('Plano de saúde'),
            'logradouro': _('Lougradouro'),
            'bairro': _('Bairro'),
        }

    def __init__(self, *args, **kwargs):
        super(matricula_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'