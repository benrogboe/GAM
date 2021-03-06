"""archivo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import include, url
from gam_app import views
from django.contrib.flatpages import views as flat_views
from dal import autocomplete
from gam_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.hmac.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('buscar/', views.search, name='search'),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('control-de-misión/', views.mission_control, name='mission_control'),
    path('persona/create/', PersonaCreate.as_view(), name='persona_create'),
    path('persona/<int:pk>/update/', PersonaUpdate.as_view(), name='persona_update'),
    path('personalookup/', PersonaNameLookup.as_view(), name='persona_name_lookup'),
    path('lugar/create/', LugarCreate.as_view(), name='lugar_create'),
    path('lugar/<int:pk>/update/', LugarUpdate.as_view(), name='lugar_update'),
    path('lugarlookup/', LugarNameLookup.as_view(), name='lugar_name_lookup'),
    path('organizacion/create/', OrganizacionCreate.as_view(), name='organizacion_create'),
    path('organizacion/<int:pk>/update/', OrganizacionUpdate.as_view(), name='organizacion_update'),
    path('organizacionlookup/', OrganizacionNameLookup.as_view(), name='organizacion_name_lookup'),
    path('autocompletar_manuscrito/', autocompletar_manuscrito.as_view(), name='autocompletar_manuscrito'),
    path('necisita_transcripción', views.necisita_transcripción, name='necisita_transcripción'),
    path('crear_usuario/', include('registration.backends.simple.urls')),
    path('file/<filename>', views.document, name='document'),
    path('editar/<filename>', views.document_edit, name='document_edit'),
    path('dzi/<file>', views.dzi, name='dzi'),
    path('caso/', views.caso, name='caso'),
    path('advanced_search_submit/', views.advanced_search_submit, name='advanced-search-submit'),
    path('sobre/', flat_views.flatpage, {'url': '/es/sobre/'}, name='sobre'),
    path('about/', flat_views.flatpage, {'url': '/en/about/'}, name='about'),
    path('documentos/', views.all_documents, name='all_documents'),
    path('portapapeles/<portapapeles>', views.espacio_de_trabajo, name='espacio_de_trabajo'),
    path('portapapeles/', views.portapapeles, name='portapapeles'),
    path('texto/', views.todo_texto, name='all_texto'),
    path('explorar/', views.explorar, name='explorar'),
    path('caso/<caso>', views.single_caso, name='single_caso'),
    path('lugar/<lugar>', views.lugar, name='lugar'),
    path('persona/<persona>', views.persona, name='persona'),
    path('procesamiento/<archivo>/<colección>/<caja>/<legajo>/<carpeta>/', views.procesamiento, name='procesamiento'),
    #paths for physical location urls
    path('<archivo>/<colección>/<caja>/<legajo>/<carpeta>/<número_de_imagen>/', views.documento5, name='documento5'),
    path('<archivo>/<colección>/<caja>/<legajo>/<carpeta>/', views.documento4, name='documento4'),
    path('<archivo>/<colección>/<caja>/<legajo>/', views.documento3, name='documento3'),
    path('<archivo>/<colección>/<caja>/', views.documento2, name='documento2'),
    path('<archivo>/<colección>/', views.documento1, name='documento1'),
    path('<archivo>/', views.documento0, name='documento0'),
)
