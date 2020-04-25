from basket.models import Basket


def current_basket(request):
    """Basket for the current user."""
    try:
        basket = request.user.basket
    except Basket.DoesNotExist:
        basket = None
    return {
        "basket": basket
    }
