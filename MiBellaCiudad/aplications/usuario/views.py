from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from .models import Usuario
from .forms import FormularioUsuario


#conect = DATABASES.

class CargarUsuario(ListView):
    
    template_name = 'usuario/usuario.html'
    model = Usuario


class Login(ListView):
    template_name = 'usuario/login.html'
    model = Usuario



class Exito(TemplateView):
    template_name = "noticia/paginaExito.html"



class UsuarioCreateView(CreateView):
    template_name = 'usuario/usuario.html'
    model = Usuario
    form_class = FormularioUsuario


    def get_success_url(self):
        print(self)
        return reverse('exito')



   