# django imports
from django import forms
from django.db import models
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# portlets imports
from lfs.catalog.settings import VARIANT
from portlets.models import Portlet

# lfs imports
from lfs.catalog.models import Category, Product


class LatestAllPortlet(Portlet):
    """A portlet for displaying latest products by given limit
    """
    class Meta:
        app_label = 'portlet'

    name = _("Latest products")

    limit = models.IntegerField(_(u"Limit"), default=15)
    #current_category = models.BooleanField(_(u"Use current category"), default=False)
    #slideshow = models.BooleanField(_(u"Slideshow"), default=False)

    @property
    def rendered_title(self):
        return self.title or self.name

    def render(self, context):
        """Renders the portlet as html.
        """
        request = context.get("request")

        latest_products = []
        products = Product.objects.filter(active=True).exclude(sub_type=VARIANT)
        # if self.current_category:
        #     obj = context.get("category") or context.get("product")
        #     if obj:
        #         category = obj if isinstance(obj, Category) else obj.get_current_category(request)
        #         categories = [category]
        #         categories.extend(category.get_all_children())
        #         filters = {"product__categories__in": categories}
        #         products = products.filter(**filters).order_by('-creation_date')[:self.limit]
        # else:
        #     products = products.order_by('-creation_date')[:self.limit]
        products = products.order_by('-creation_date')[:self.limit]

        for product in products:
            if product.is_product_with_variants() and product.has_variants():
                latest_products.append(product.get_default_variant())
            else:
                latest_products.append(product)

        return render_to_string("lfs/portlets/latest_all.html", RequestContext(request, {
            "title": self.rendered_title,            
            "products": latest_products
        }))

    def form(self, **kwargs):
        """
        """
        return LatestAllForm(instance=self, **kwargs)

    def __unicode__(self):
        return u"%s" % self.id


class LatestAllForm(forms.ModelForm):
    """
    """
    class Meta:
        model = LatestAllPortlet
