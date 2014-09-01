from django.shortcuts import render_to_response
from curriculum.models import TipoProyecto
from django.conf import settings

# Create your views here.
def home(request):
    menuInicio = 'selected'
    return render_to_response('default/index.html', {'menuInicio': menuInicio,
      'settings': settings, })

def estudios(request):
    menuEstudios = 'selected'
    return render_to_response('default/estudios.html', 
                              {'menuEstudios': menuEstudios,
                                'settings': settings, })

def proyectos(request):
    menuProyectos = 'selected'
    tipoProyectos = TipoProyecto.objects.all()
    return render_to_response('default/proyectos.html',
                              {'tipoProyectos': tipoProyectos, 
                               'menuProyectos': menuProyectos,
                               'settings': settings, })

def contacto(request):
    menuContacto = 'selected'
    return render_to_response('default/contacto.html', 
                              {'menuContacto': menuContacto,
                                'settings': settings, })
