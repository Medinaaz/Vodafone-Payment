from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from comment.forms import CommentForm
from product.models import Product, StatusChoices
from user.forms import RegistrationForm, LoginForm


class ProductDetailsView(TemplateView):
    template_name = "product/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get("slug")
        product = Product.objects.filter(
            slug=slug, status=StatusChoices.PUBLIC
        ).select_related("category").prefetch_related("images", "tags").first()
        if not product:
            raise Http404(_(f"Product {slug} was not found!"))
        context["product"] = product
        context["product_category"] = product.category
        context["main_properties"] = product.properties.filter(is_main_property=True).select_related("option")
        context["additional_properties"] = product.properties.all().select_related("option")
        context["comments"] = product.comments.filter(verified=True, message__isnull=False).exclude(message="")
        context["comment_form"] = CommentForm()
        context["reg_form"] = RegistrationForm()
        context["login_form"] = LoginForm()
        return context
