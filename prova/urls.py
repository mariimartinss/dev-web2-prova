"""
URL configuration for prova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #    path('admin/', admin.site.urls),
    path ('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path("painel/", views.painel, name="painel"),
    path("editar/<int:id>/", views.editar, name="editar"),
    path("visualizar/<int:id>/", views.visualizar, name="visualizar"),
    path("excluir/<int:id>/", views.excluir, name="excluir"),


]
