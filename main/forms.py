from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import ALuno

class ALunoForm(forms.ModelForm):
    class Meta:
        model = ALuno
        fields = ['nome', 'telefone', 'email', 'data_nascimento', 'descricao']
    
    def __init__(self, *args, **kwargs):
        super(ALunoForm, self).__init__(*args, *kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['telefone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['data_nascimento'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['class'] = 'form-control'