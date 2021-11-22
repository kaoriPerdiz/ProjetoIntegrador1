from django.db import models

class matricula(models.Model):
    nome_crianca = models.CharField(max_length=50)
    data_nascimento_crianca = models.DateField()
    nome_mae = models.CharField(max_length=50)
    telefone_mae = models.CharField(max_length=15)
    servico_mae = models.CharField(max_length=50, null=True)
    telefone_servico_mae = models.CharField(max_length=15, null=True)
    nome_pai = models.CharField(max_length=50)
    telefone_pai = models.CharField(max_length=15)
    servico_pai = models.CharField(max_length=50, null=True)
    telefone_servico_pai = models.CharField(max_length=15, null=True)
    cuidado_medico_observacao = models.CharField(max_length=100, null=True)
    cuidado_medico_plano_saude = models.CharField(max_length=30, null=True)
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    turma = models.ForeignKey('turmaApp.turma', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nome_crianca
