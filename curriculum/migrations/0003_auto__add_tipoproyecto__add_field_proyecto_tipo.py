# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoProyecto'
        db.create_table(u'curriculum_tipoproyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'curriculum', ['TipoProyecto'])

        # Adding field 'Proyecto.tipo'
        db.add_column(u'curriculum_proyecto', 'tipo',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curriculum.TipoProyecto'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TipoProyecto'
        db.delete_table(u'curriculum_tipoproyecto')

        # Deleting field 'Proyecto.tipo'
        db.delete_column(u'curriculum_proyecto', 'tipo_id')


    models = {
        u'curriculum.areatecnica': {
            'Meta': {'object_name': 'AreaTecnica'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'curriculum.empresa': {
            'Meta': {'object_name': 'Empresa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'curriculum.idioma': {
            'Meta': {'object_name': 'Idioma'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'curriculum.pais': {
            'Meta': {'object_name': 'Pais'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'curriculum.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'empresas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['curriculum.Empresa']", 'symmetrical': 'False'}),
            'enCurso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fechaDesde': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 20, 0, 0)'}),
            'fechaHasta': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 20, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curriculum.Idioma']", 'null': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modalidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curriculum.Pais']", 'null': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curriculum.TipoProyecto']", 'null': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'curriculum.tareaproyecto': {
            'Meta': {'object_name': 'TareaProyecto'},
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['curriculum.AreaTecnica']", 'symmetrical': 'False', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curriculum.Proyecto']"})
        },
        u'curriculum.tipoproyecto': {
            'Meta': {'object_name': 'TipoProyecto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['curriculum']