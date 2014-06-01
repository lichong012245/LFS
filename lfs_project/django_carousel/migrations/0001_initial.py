# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carousel'
        db.create_table(u'django_carousel_carousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carousel_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_carousel', ['Carousel'])

        # Adding M2M table for field carousel_entries on 'Carousel'
        m2m_table_name = db.shorten_name(u'django_carousel_carousel_carousel_entries')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('carousel', models.ForeignKey(orm[u'django_carousel.carousel'], null=False)),
            ('carouselentry', models.ForeignKey(orm[u'django_carousel.carouselentry'], null=False))
        ))
        db.create_unique(m2m_table_name, ['carousel_id', 'carouselentry_id'])

        # Adding model 'CarouselEntryTranslation'
        db.create_table(u'django_carousel_carouselentry_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text_over_image', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('navigation_entry', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['django_carousel.CarouselEntry'])),
        ))
        db.send_create_signal(u'django_carousel', ['CarouselEntryTranslation'])

        # Adding unique constraint on 'CarouselEntryTranslation', fields ['language_code', 'master']
        db.create_unique(u'django_carousel_carouselentry_translation', ['language_code', 'master_id'])

        # Adding model 'CarouselEntry'
        db.create_table(u'django_carousel_carouselentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text_background_color', self.gf('paintstore.fields.ColorPickerField')(max_length=7, blank=True)),
            ('image', self.gf(u'django.db.models.fields.files.ImageField')(max_length=100)),
            ('cropped', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'django_carousel', ['CarouselEntry'])


    def backwards(self, orm):
        # Removing unique constraint on 'CarouselEntryTranslation', fields ['language_code', 'master']
        db.delete_unique(u'django_carousel_carouselentry_translation', ['language_code', 'master_id'])

        # Deleting model 'Carousel'
        db.delete_table(u'django_carousel_carousel')

        # Removing M2M table for field carousel_entries on 'Carousel'
        db.delete_table(db.shorten_name(u'django_carousel_carousel_carousel_entries'))

        # Deleting model 'CarouselEntryTranslation'
        db.delete_table(u'django_carousel_carouselentry_translation')

        # Deleting model 'CarouselEntry'
        db.delete_table(u'django_carousel_carouselentry')


    models = {
        u'django_carousel.carousel': {
            'Meta': {'object_name': 'Carousel'},
            'carousel_entries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'carousel'", 'blank': 'True', 'to': u"orm['django_carousel.CarouselEntry']"}),
            'carousel_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'django_carousel.carouselentry': {
            'Meta': {'ordering': "('order',)", 'object_name': 'CarouselEntry'},
            'cropped': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'text_background_color': ('paintstore.fields.ColorPickerField', [], {'max_length': '7', 'blank': 'True'})
        },
        u'django_carousel.carouselentrytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'CarouselEntryTranslation', 'db_table': "u'django_carousel_carouselentry_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['django_carousel.CarouselEntry']"}),
            'navigation_entry': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'text_over_image': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['django_carousel']