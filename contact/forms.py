from logging import PlaceHolder
from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'}))
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'Digite seu email'}))
    mensagem = forms.CharField(label="Mensagem", max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Digite o assunto'}))