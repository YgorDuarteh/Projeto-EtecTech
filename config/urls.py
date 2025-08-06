from django.contrib import admin
from django.urls import path
from cursos.views import IndexView, InscreverCursoView, CursoDetailView
from usuarios.views import usuario_view, login_view, logout_view

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', usuario_view, name='usuario'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='curso_detail'),
    path('curso/<int:curso_id>/inscrever/', InscreverCursoView.as_view(), name='inscrever_curso'),
]

