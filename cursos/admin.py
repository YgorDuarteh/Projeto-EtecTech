from django.contrib import admin
from .models import Categoria, Instrutor, Curso, Modulo, Aula, Inscricao

admin.site.register(Categoria)
admin.site.register(Instrutor)
admin.site.register(Curso)
admin.site.register(Modulo)
admin.site.register(Aula)
admin.site.register(Inscricao)
