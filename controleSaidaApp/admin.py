from django.contrib import admin
from .models import pessoas_autorizadas, controle_saida

# Register your models here.
admin.site.register(pessoas_autorizadas)
admin.site.register(controle_saida)