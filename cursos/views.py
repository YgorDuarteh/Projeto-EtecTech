from .models import Curso, Inscricao
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.contrib import messages

class IndexView(ListView):
    model = Curso
    template_name = 'index.html'
    context_object_name = 'cursos'

    def get_queryset(self):
        queryset = super().get_queryset() .order_by('titulo')
        titulo = self.request.GET.get('titulo')

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
    
        return queryset
    
class CursoDetailView(DetailView):
    model = Curso
    template_name = 'curso_detail.html'
    context_object_name = 'curso'

@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class InscreverCursoView(ListView):
    def post(self, request, curso_id):
        curso = get_object_or_404(Curso, pk=curso_id)
        usuario = request.user

        if not Inscricao.objects.filter(curso=curso, usuario=usuario).exists():
            Inscricao.objects.create(curso=curso, usuario=usuario)
            messages.sucess(request, 'Inscrição realizada com sucesso!')
        else:
            messages.warning(request, 'Você já está inscrito neste curso.')

        return redirect('curso_detail', pk=curso_id)