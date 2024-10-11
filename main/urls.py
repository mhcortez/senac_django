from django.urls import path
from .import views
from .views import aluno

urlpatterns = [
    #path('', views.index, name='index'),
    path('aluno', views.aluno, name='aluno'),
]

