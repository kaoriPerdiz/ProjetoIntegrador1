from django.db import models
from datetime import date

# Create your models here.
class pessoas_autorizadas(models.Model):
    crianca = models.ForeignKey('matriculaApp.matricula', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.nome + " (" + self.parentesco + ") - Aluno: " + self.crianca.nome_crianca

class controle_saida(models.Model):
    crianca = models.ForeignKey('matriculaApp.matricula', on_delete=models.CASCADE)
    responsavel = models.ForeignKey(pessoas_autorizadas, on_delete=models.CASCADE)
    data_saida = models.DateField()
    def __str__(self) -> str:
        return self.crianca.nome_crianca + " - Pessoa autorizada: " + self.responsavel.nome + " - " + str(self.data_saida.strftime("%d/%m/%Y"))