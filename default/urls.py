from django.conf.urls import include, url
from django.contrib import admin
from default import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^estudios$', views.estudios, name='estudios'),
    url(r'^proyectos$', views.proyectos, name='proyectos'),
    url(r'^contacto$', views.contacto, name='contacto'),
]
