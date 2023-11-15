from django.db import models, migrations

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    telefone = models.CharField(max_length=15, default='')
    setor = models.CharField(max_length=40, default='')
