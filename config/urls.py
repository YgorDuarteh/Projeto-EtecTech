from django.contrib import admin
from django.urls import path
from usuarios.views import usuario_view, login_view, logout_view
from cursos.views import CursoListView

urlpatterns = [
    path('',CursoListView.as_view(), name='cursos_list'),
    path('admin/', admin.site.urls),
    path('users/', usuario_view, name='usuario'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
]

