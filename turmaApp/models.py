from django.db import models

# Create your models here.
class turma(models.Model):
    nome_turma = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    nome_professor_monitor = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nome_turma + " - Professor(a)/monitor(a): " + self.nome_professor_monitor