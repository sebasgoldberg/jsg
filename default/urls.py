from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'default.views.home', name='home'),
    url(r'^estudios$', 'default.views.estudios', name='estudios'),
    url(r'^proyectos$', 'default.views.proyectos', name='proyectos'),
    url(r'^contacto$', 'default.views.contacto', name='contacto'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT}),
)
