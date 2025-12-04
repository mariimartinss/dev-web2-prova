from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Impede salvar senha em texto
        if not self.senha.startswith("pbkdf2_"):
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


