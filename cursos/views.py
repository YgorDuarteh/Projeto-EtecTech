from .models import Curso
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

class CursoListView(ListView):
    model = Curso
    template_name = 'ListaCursos.html'
    context_object_name = 'cursos'

    def get_queryset(self):
        cursos = super().get_queryset() .order_by('titulo')
        titulo = self.request.GET.get('titulo')

        if titulo:
            cursos = cursos.filter(titulo__icontains=titulo)
    
        return cursos