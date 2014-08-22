from django.contrib import admin
from curriculum.models import Proyecto, AreaTecnica, Empresa, TareaProyecto, Idioma, Pais, TipoProyecto

# Register your models here.
class TareaProyectoInline(admin.TabularInline):
    model = TareaProyecto
    extra = 0

class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields=['id']
    inlines=[TareaProyectoInline]
    list_display=['id','titulo', 'fechaDesde', 'fechaHasta', 'idioma', 'pais', 'modalidad']
    list_display_links = ('id', 'titulo')
    search_fields=['titulo']
    list_per_page = 40

admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(AreaTecnica)
admin.site.register(Empresa)
admin.site.register(Idioma)
admin.site.register(Pais)
admin.site.register(TipoProyecto)
