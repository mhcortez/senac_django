from django.shortcuts import render
from .models import ALuno
from .forms import ALunoForm
from django.http import HttpResponse

def aluno(request):
    aluno = ALuno.objects.all()
    return render(request, 'main/aluno.html', {'aluno': aluno})