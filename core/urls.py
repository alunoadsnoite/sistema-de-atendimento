
from django.contrib import admin
from django.urls import path
from atendimento import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('fila/', views.fila, name='fila'),
    path('banco/', views.banco, name='banco'),
]
