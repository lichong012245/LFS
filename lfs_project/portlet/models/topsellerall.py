# django imports
from django import forms
from django.db import models
from django.template import RequestContext
from django.template.loader import render_to_string
from django.db.models import Q
from django.db import connection

# portlets imports
from portlets.models import Portlet

# lfs imports
import lfs.catalog.utils
import lfs.catalog.models
import lfs.marketing.utils
from lfs.catalog.models import Product
from lfs.marketing.models import Topseller



class TopsellerPortletAll(Portlet):
    """Portlet to display all top sold products.
    """
    limit = models.IntegerField(default=100)

    class Meta:
        app_label = 'portlet'

    def __unicode__(self):
        return u"%s" % self.id

    def render(self, context):
        """Renders the portlet as html.
        """
        request = context.get("request")
        # object = context.get("category") or context.get("product")
        # if object is None:
        #     topseller = lfs.marketing.utils.get_topseller(self.limit)
        # elif isinstance(object, lfs.catalog.models.Product):
        #     category = object.get_current_category(context.get("request"))
        #     topseller = lfs.marketing.utils.get_topseller_for_category(
        #         category, self.limit)
        # else:
        #     topseller = lfs.marketing.utils.get_topseller_for_category(
        #         object, self.limit)
        topseller = self.get_topseller()

        return render_to_string("lfs/portlets/topseller_all.html", RequestContext(request, {
            "title": self.title,
            "topseller": topseller,
        }))

    def form(self, **kwargs):
        return TopsellerAllForm(instance=self, **kwargs)

    def get_topseller(self):
        """Returns all products with the most sales."""    

    # TODO: Check Django 1.1's aggregation
        cursor = connection.cursor()
        cursor.execute("""SELECT product_id, sum(product_amount) as sum
                      FROM order_orderitem
                      where product_id is not null
                      GROUP BY product_id
                      ORDER BY sum DESC""")

        products = []
        for topseller in cursor.fetchall():
            product = Product.objects.get(pk=topseller[0])
            if product.is_active():
                try:
                    products.append(product)
                except Product.DoesNotExist:
                    pass

        for explicit_ts in Topseller.objects.all():

            if explicit_ts.product.is_active():
            # Remove explicit_ts if it's already in the object list
                if explicit_ts.product in products:
                    products.pop(products.index(explicit_ts.product))

            # Then reinsert the explicit_ts on the given position
                position = explicit_ts.position - 1
                if position < 0:
                    position = 0
                products.insert(position, explicit_ts.product)        
        return products


class TopsellerAllForm(forms.ModelForm):
    """Form for the TopsellerAllPortlet.
    """
    class Meta:
        model = TopsellerPortletAll
