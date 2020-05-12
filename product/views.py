from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from product.models import Product


class ProductDetailsView(TemplateView):
    template_name = "product/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get("slug")
        product = Product.objects.filter(
            slug=slug, status=2
        ).select_related("category").prefetch_related("images", "tags").first()
        if not product:
            raise Http404(_("Product {slug} was not found!".format(slug=slug)))
        context["product"] = product
        context["product_category"] = product.category
        context["main_properties"] = product.properties.filter(is_main_property=True).select_related("option")
        context["additional_properties"] = product.properties.filter(is_main_property=False).select_related("option")
        return context
