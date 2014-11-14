# coding=utf-8
from django.db import models
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

MODALIDAD_FULL_TIME = 0
MODALIDAD_FREELANCE = 1

MODALIDAD = (
             (MODALIDAD_FULL_TIME, _(u'Full Time')),
             (MODALIDAD_FREELANCE, _(u'Freelance')),
             )

DICT_MODALIDAD = dict(MODALIDAD)

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name=_(u'Nombre'), 
                              unique=True)

    def __unicode__(self):
        return self.nombre

class Idioma(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name=_(u'Descripción'), 
                              unique=True)

    def __unicode__(self):
        return self.descripcion

class Pais(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name=_(u'Descripción'), 
                              unique=True)

    def __unicode__(self):
        return self.descripcion

class TipoProyecto(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name=_(u'Descripción'), 
                              unique=True)

    def __unicode__(self):
        return self.descripcion

    def get_proyectos_ordenados_por_fecha(self):
        for proyecto in self.proyecto_set.all().order_by('-fechaDesde'):
            yield proyecto

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=_(u'Título'), 
                              unique=True)

    tipo = models.ForeignKey(TipoProyecto, verbose_name=_(u'Tipo de proyecto'), null=True, blank=False)
 
    fechaDesde = models.DateField( verbose_name=_(u'Fecha desde'),
                                          null=False, blank=False, 
                                          default=datetime.datetime.now())
    enCurso = models.BooleanField(default=False, 
                                  verbose_name=_(u'En curso'))

    fechaHasta = models.DateField( verbose_name=_(u'Fecha hasta'),
                                          null=True, blank=True,
                                          default=datetime.datetime.now())

    idioma = models.ForeignKey(Idioma, verbose_name=_(u'Idioma'), null=True, blank=False)
 
    pais = models.ForeignKey(Pais, verbose_name=_(u'Pais'), null=True, blank=False)

    modalidad = models.IntegerField(verbose_name=_(u'Modalidad'), 
                                    choices=MODALIDAD, 
                                    default=MODALIDAD_FULL_TIME)
    empresas = models.ManyToManyField(Empresa, blank=False, verbose_name=_(u'Empresas'))
    #clientes = models.ManyToManyField(Empresa, blank=False, verbose_name=_(u'Clientes'))

    img = models.ImageField(verbose_name=_(u'Imagen'), 
                               upload_to='proyectos/', blank=False)
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(100,100)],
        source='img', format='JPEG', options={'quality': 90})

    def __unicode__(self):
        return self.titulo
    
    def getDescripcionDuracion(self):
        if self.enCurso:
            fechaHasta = _(u'Fecha actual')
        else:
            fechaHasta = self.fechaHasta.strftime("%Y/%m")
        return _(u'%s a %s') % (self.fechaDesde.strftime("%Y/%m"), fechaHasta)

    def getDescripcionModalidad(self):
        return DICT_MODALIDAD[self.modalidad]

    def getTareas(self):
        return self.tareaproyecto_set.all()

class AreaTecnica(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name=_(u'Descripción'), 
                              unique=True)

    def __unicode__(self):
        return self.descripcion

    class Meta:
      ordering = ['descripcion', ]


class TareaProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, verbose_name=_(u'Proyecto'))
    areas = models.ManyToManyField(AreaTecnica, blank=True, verbose_name=_(u'Areas'))
    descripcion = models.TextField(blank=True, verbose_name=_(u'Descripción'))

    def __unicode__(self):
        return self.descripcion

