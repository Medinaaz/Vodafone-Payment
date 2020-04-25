from django.views.generic import TemplateView

from basket.models import Basket, BasketItem


class BasketDetailView(TemplateView):
    template_name = "basket/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

        try:
            basket = Basket.objects.get(
                user=self.request.user,
            )
        except (Basket.DoesNotExist, Basket.MultipleObjectsReturned):
            basket = None

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
