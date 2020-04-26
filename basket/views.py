from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, View
from django.http import JsonResponse

from basket.models import Basket, BasketItem
from product.models import Product


class BasketDetailView(TemplateView):
    template_name = "basket/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

        basket = Basket.current_basket(user=self.request.user)

        basket_items = BasketItem.objects.filter(
            basket=basket,
        )
        context['basket_items'] = basket_items

        subtotal = sum(basket_item.product.price for basket_item in basket_items)
        context['subtotal'] = subtotal

        total = 0
        if basket:
            total = basket.coupon_code.get_discounted_value(subtotal) if basket.coupon_code else subtotal
        context['total'] = total

        context['discount'] = total - subtotal

        return context


class BasketManagementAjaxView(View):
    def __init__(self, *args, **kwargs):
        self.basket = None
        super(BasketManagementAjaxView, self).__init__(*args, **kwargs)

    def serialize_basket(self) -> dict:
        """Serialize simple basket details without item details."""
        return {
            "total": self.basket.total
        }

    def get(self, request, **kwargs):
        """Get basket details."""
        raise NotImplementedError

    def post(self, request, **kwargs):
        """Add product to the basket."""
        self.basket = Basket.current_basket(user=request.user)
        product_slug = request.POST.get("product_slug")
        if not product_slug:
            return JsonResponse(
                {"code": "missing_product_slug", "message": _("Product information was not found.")},
                safe=False, status=400
            )
        product = Product.objects.filter(slug=product_slug).first()
        if not product:
            return JsonResponse(
                {"code": "product_not_found", "message": _("Product information was not found.")},
                safe=False, status=404
            )
        try:
            quantity = int(request.POST.get("quantity", 1))
        except ValueError:
            return JsonResponse(
                {"code": "incorrect_quantity", "message": _("Please, specify a quantity for the item!")},
                safe=False, status=400
            )
        if quantity < 1:
            return JsonResponse(
                {"code": "incorrect_quantity", "message": _("Please, specify a quantity for the item!")},
                safe=False, status=400
            )
        try:
            basket_item = BasketItem.objects.get(basket=self.basket, product=product)
            basket_item.quantity = quantity
            basket_item.save()
        except BasketItem.DoesNotExist:
            basket_item = BasketItem.objects.create(
                basket=self.basket, product=product, quantity=quantity
            )
        self.basket = self.basket.update_total_amount(commit=True)
        basket_data = self.serialize_basket()
        return JsonResponse(
            {"code": "success", "message": _("Basket updated"), "item_id": basket_item.pk, **basket_data},
            safe=False, status=200
        )

    def patch(self, request, **kwargs):
        """Update quantity and other product details."""
        raise NotImplementedError

    def delete(self, request, **kwargs):
        """Remove the product from basket."""
        raise NotImplementedError
