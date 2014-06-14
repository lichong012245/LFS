# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Carousel'
        db.create_table('django_carousel_carousel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carousel_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('django_carousel', ['Carousel'])

        # Adding M2M table for field carousel_entries on 'Carousel'
        db.create_table('django_carousel_carousel_carousel_entries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('carousel', models.ForeignKey(orm['django_carousel.carousel'], null=False)),
            ('carouselentry', models.ForeignKey(orm['django_carousel.carouselentry'], null=False))
        ))
        db.create_unique('django_carousel_carousel_carousel_entries', ['carousel_id', 'carouselentry_id'])

        # Adding model 'CarouselEntryTranslation'
        db.create_table('django_carousel_carouselentry_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text_over_image', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('navigation_entry', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['django_carousel.CarouselEntry'])),
        ))
        db.send_create_signal('django_carousel', ['CarouselEntryTranslation'])

        # Adding unique constraint on 'CarouselEntryTranslation', fields ['language_code', 'master']
        db.create_unique('django_carousel_carouselentry_translation', ['language_code', 'master_id'])

        # Adding model 'CarouselEntry'
        db.create_table('django_carousel_carouselentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf(u'django.db.models.fields.files.ImageField')(max_length=100)),
            ('cropped', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('text_background_color', self.gf('paintstore.fields.ColorPickerField')(max_length=7, blank=True)),
        ))
        db.send_create_signal('django_carousel', ['CarouselEntry'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'CarouselEntryTranslation', fields ['language_code', 'master']
        db.delete_unique('django_carousel_carouselentry_translation', ['language_code', 'master_id'])

        # Deleting model 'Carousel'
        db.delete_table('django_carousel_carousel')

        # Removing M2M table for field carousel_entries on 'Carousel'
        db.delete_table('django_carousel_carousel_carousel_entries')

        # Deleting model 'CarouselEntryTranslation'
        db.delete_table('django_carousel_carouselentry_translation')

        # Deleting model 'CarouselEntry'
        db.delete_table('django_carousel_carouselentry')


    models = {
        'django_carousel.carousel': {
            'Meta': {'object_name': 'Carousel'},
            'carousel_entries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'carousel'", 'blank': 'True', 'to': "orm['django_carousel.CarouselEntry']"}),
            'carousel_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'django_carousel.carouselentry': {
            'Meta': {'ordering': "('order',)", 'object_name': 'CarouselEntry'},
            'cropped': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'text_background_color': ('paintstore.fields.ColorPickerField', [], {'max_length': '7', 'blank': 'True'})
        },
        'django_carousel.carouselentrytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'CarouselEntryTranslation', 'db_table': "'django_carousel_carouselentry_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['django_carousel.CarouselEntry']"}),
            'navigation_entry': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'text_over_image': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['django_carousel']
