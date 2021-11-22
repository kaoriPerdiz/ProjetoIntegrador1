from django.db import models

# Create your models here.
class frequencia(models.Model):
    crianca = models.ForeignKey('matriculaApp.matricula', on_delete=models.CASCADE)
    data_presenca = models.DateField()
    presente = models.BooleanField()
    def __str__(self) -> str:
        return super().__str__()

