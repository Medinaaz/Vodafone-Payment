from django.urls import path

from basket.views import BasketDetailView, BasketManagementAjaxView

urlpatterns = [
    path("manage/", BasketManagementAjaxView.as_view(), name="basket_management_ajax"),
    path('', BasketDetailView.as_view(), name="basket"),
]
