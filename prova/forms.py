from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(),
        label="Senha"
    )

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
