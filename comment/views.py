from django.http import Http404
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView

from comment.forms import CommentForm
from comment.models import Comment
from product.models import Product


class BasicCommandCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def __init__(self):
        self.object = None
        super().__init__()

    def form_valid(self, form):
        try:
            product = Product.objects.get(slug=self.kwargs.get("slug"))
        except Product.DoesNotExist:
            raise Http404(_("Product not found!"))
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.product = product
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("product_details", args=[self.kwargs.get("slug")])
