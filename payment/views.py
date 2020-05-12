from django.shortcuts import render
from django.views.generic import TemplateView
from basket.models import Basket, BasketItem
from shipment.models import Shipment
# Create your views here.

class PaymentView(TemplateView):
    template_name = "payment/detail.html"

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
