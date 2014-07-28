# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LatestAllPortlet'
        db.create_table('portlet_latestallportlet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('limit', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('current_category', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('portlet', ['LatestAllPortlet'])

        # Adding model 'LatestPortlet'
        db.create_table('portlet_latestportlet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('limit', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('current_category', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slideshow', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('portlet', ['LatestPortlet'])

        # Adding model 'TopsellerPortletAll'
        db.create_table('portlet_topsellerportletall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('limit', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal('portlet', ['TopsellerPortletAll'])

        # Adding field 'FilterPortlet.show_manufacturer_filters'
        db.add_column('portlet_filterportlet', 'show_manufacturer_filters',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'LatestAllPortlet'
        db.delete_table('portlet_latestallportlet')

        # Deleting model 'LatestPortlet'
        db.delete_table('portlet_latestportlet')

        # Deleting model 'TopsellerPortletAll'
        db.delete_table('portlet_topsellerportletall')

        # Deleting field 'FilterPortlet.show_manufacturer_filters'
        db.delete_column('portlet_filterportlet', 'show_manufacturer_filters')


    models = {
        'portlet.averageratingportlet': {
            'Meta': {'object_name': 'AverageRatingPortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.cartportlet': {
            'Meta': {'object_name': 'CartPortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.categoriesportlet': {
            'Meta': {'object_name': 'CategoriesPortlet'},
            'expand_level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.deliverytimeportlet': {
            'Meta': {'object_name': 'DeliveryTimePortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.featuredportlet': {
            'Meta': {'object_name': 'FeaturedPortlet'},
            'current_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'slideshow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.filterportlet': {
            'Meta': {'object_name': 'FilterPortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_manufacturer_filters': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_price_filters': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_product_filters': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.forsaleportlet': {
            'Meta': {'object_name': 'ForsalePortlet'},
            'current_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'slideshow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.latestallportlet': {
            'Meta': {'object_name': 'LatestAllPortlet'},
            'current_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.latestportlet': {
            'Meta': {'object_name': 'LatestPortlet'},
            'current_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'slideshow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.pagesportlet': {
            'Meta': {'object_name': 'PagesPortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.recentproductsportlet': {
            'Meta': {'object_name': 'RecentProductsPortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.relatedproductsportlet': {
            'Meta': {'object_name': 'RelatedProductsPortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.textportlet': {
            'Meta': {'object_name': 'TextPortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.topsellerportlet': {
            'Meta': {'object_name': 'TopsellerPortlet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'portlet.topsellerportletall': {
            'Meta': {'object_name': 'TopsellerPortletAll'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['portlet']