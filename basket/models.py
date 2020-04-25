from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import Product
from user.models import User
from .utils import get_random_code


class Basket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='basket',
    )
    coupon_code = models.ForeignKey(
        to='Coupon',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"Basket#{self.id}"


class BasketItem(models.Model):
    class Size(models.TextChoices):
        NONE = 'N', _("None")
        SMALL = 'S', _("Small")
        MEDIUM = 'M', _("Medium")
        LARGE = 'L', _("Large")

    class Color(models.TextChoices):
        NONE = 'none', _("None")
        BLACK = 'black', _("Black")
        WHITE = 'white', _("White")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    size = models.CharField(
        max_length=4,
        choices=Size.choices,
        default=Size.NONE,
    )
    color = models.CharField(
        max_length=16,
        choices=Color.choices,
        default=Color.NONE,
    )

    class Meta:
        verbose_name = _("basket item")
        verbose_name_plural = _("basket items")

    def __str__(self):
        return f"{self.product}"


# Coupon Codes

class Ruleset(models.Model):
    allowed_users = models.ForeignKey(
        to='AllowedUsersRule',
        on_delete=models.CASCADE,
        verbose_name=_("allowed users rule"),
    )
    max_uses = models.ForeignKey(
        to='MaxUsesRule',
        on_delete=models.CASCADE,
        verbose_name=_("max uses rule"),
    )
    validity = models.ForeignKey(
        to='ValidityRule',
        on_delete=models.CASCADE,
        verbose_name=_("validity rule"),
    )

    class Meta:
        verbose_name = _("ruleset")
        verbose_name_plural = _("rulesets")

    def __str__(self):
        return "Ruleset Nº{0}".format(self.id)


class AllowedUsersRule(models.Model):
    users = models.ManyToManyField(
        to=User,
        blank=True,
        verbose_name=_("users"),
    )
    all_users = models.BooleanField(
        default=False,
        verbose_name=_("all users?"),
    )

    class Meta:
        verbose_name = _("allowed users rule")
        verbose_name_plural = _("allowed users rules")

    def __str__(self):
        return "AllowedUsersRule Nº{0}".format(self.id)


class MaxUsesRule(models.Model):
    max_uses = models.BigIntegerField(default=0, verbose_name=_("maximum uses"))
    is_infinite = models.BooleanField(default=False, verbose_name=_("infinite uses?"))
    uses_per_user = models.IntegerField(default=1, verbose_name=_("uses per user"))

    class Meta:
        verbose_name = _("max uses rule")
        verbose_name_plural = _("max uses rules")

    def __str__(self):
        return "MaxUsesRule Nº{0}".format(self.id)


class ValidityRule(models.Model):
    expiration_date = models.DateTimeField(verbose_name=_("expiration date"))
    is_active = models.BooleanField(default=False, verbose_name=_("is active?"))

    class Meta:
        verbose_name = _("validity rule")
        verbose_name_plural = _("validity rules")

    def __str__(self):
        return "ValidityRule Nº{0}".format(self.id)


class CouponUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE, verbose_name=_("coupon"))
    times_used = models.IntegerField(default=0, editable=False, verbose_name=_("times used"))

    class Meta:
        verbose_name = _("coupon user")
        verbose_name_plural = _("coupon users")

    def __str__(self):
        return str(self.user)


class Discount(models.Model):
    value = models.IntegerField(default=0, verbose_name=_("value"))
    is_percentage = models.BooleanField(default=False, verbose_name=_("is percentage?"))

    class Meta:
        verbose_name = _("discount")
        verbose_name_plural = _("discounts")

    def __str__(self):
        if self.is_percentage:
            return "{0}% - Discount".format(self.value)
        return "{0} - Discount".format(self.value)


class Coupon(models.Model):
    code = models.CharField(
        max_length=12,
        default=get_random_code,
        unique=True,
        verbose_name=_("coupon code"),
    )
    discount = models.ForeignKey(
        to='Discount',
        on_delete=models.CASCADE,
    )
    times_used = models.IntegerField(
        default=0,
        editable=False,
        verbose_name=_("times used"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at"),
    )
    ruleset = models.ForeignKey(
        to='Ruleset',
        on_delete=models.CASCADE,
        verbose_name=_("ruleset"),
    )

    class Meta:
        verbose_name = _("coupon")
        verbose_name_plural = _("coupons")

    def __str__(self):
        return self.code

    def use_coupon(self, user):
        coupon_user, created = CouponUser.objects.get_or_create(
            user=user,
            coupon=self,
        )
        coupon_user.times_used += 1
        coupon_user.save()
        self.times_used += 1
        self.save()

    def get_discount(self):
        return {
            "value": self.discount.value,
            "is_percentage": self.discount.is_percentage
        }

    def get_discounted_value(self, initial_value):
        discount = self.get_discount()
        if discount['is_percentage']:
            new_price = initial_value - ((initial_value * discount['value']) / 100)
            new_price = new_price if new_price >= 0.0 else 0.0
        else:
            new_price = initial_value - discount['value']
            new_price = new_price if new_price >= 0.0 else 0.0
        return new_price
