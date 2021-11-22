from django.db import models

# Create your models here.
class bilhete(models.Model):
    mensagem = models.CharField(max_length=1000)
    def __str__(self) -> str:
        return super().__str__()
