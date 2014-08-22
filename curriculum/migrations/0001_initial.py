# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empresa'
        db.create_table(u'curriculum_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'curriculum', ['Empresa'])

        # Adding model 'Idioma'
        db.create_table(u'curriculum_idioma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'curriculum', ['Idioma'])

        # Adding model 'Proyecto'
        db.create_table(u'curriculum_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('fechaDesde', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 20, 0, 0))),
            ('enCurso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fechaHasta', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 20, 0, 0), null=True, blank=True)),
            ('idioma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curriculum.Idioma'], null=True)),
            ('modalidad', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'curriculum', ['Proyecto'])

        # Adding M2M table for field empresas on 'Proyecto'
        m2m_table_name = db.shorten_name(u'curriculum_proyecto_empresas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm[u'curriculum.proyecto'], null=False)),
            ('empresa', models.ForeignKey(orm[u'curriculum.empresa'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyecto_id', 'empresa_id'])

        # Adding model 'AreaTecnica'
        db.create_table(u'curriculum_areatecnica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'curriculum', ['AreaTecnica'])

        # Adding model 'TareaProyecto'
        db.create_table(u'curriculum_tareaproyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curriculum.Proyecto'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'curriculum', ['TareaProyecto'])

        # Adding M2M table for field areas on 'TareaProyecto'
        m2m_table_name = db.shorten_name(u'curriculum_tareaproyecto_areas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tareaproyecto', models.ForeignKey(orm[u'curriculum.tareaproyecto'], null=False)),
            ('areatecnica', models.ForeignKey(orm[u'curriculum.areatecnica'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tareaproyecto_id', 'areatecnica_id'])


    def backwards(self, orm):
        # Deleting model 'Empresa'
        db.delete_table(u'curriculum_empresa')

        # Deleting model 'Idioma'
        db.delete_table(u'curriculum_idioma')

        # Deleting model 'Proyecto'
        db.delete_table(u'curriculum_proyecto')

        # Removing M2M table for field empresas on 'Proyecto'
        db.delete_table(db.shorten_name(u'curriculum_proyecto_empresas'))

        # Deleting model 'AreaTecnica'
        db.delete_table(u'curriculum_areatecnica')

        # Deleting model 'TareaProyecto'
        db.delete_table(u'curriculum_tareaproyecto')

        # Removing M2M table for field areas on 'TareaProyecto'
        db.delete_table(db.shorten_name(u'curriculum_tareaproyecto_areas'))


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
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'curriculum.tareaproyecto': {
            'Meta': {'object_name': 'TareaProyecto'},
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['curriculum.AreaTecnica']", 'symmetrical': 'False', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curriculum.Proyecto']"})
        }
    }

    complete_apps = ['curriculum']