from django.contrib import admin
from django.urls import path

from core.views import HomePageView
from product.views import ProductDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/<slug:slug>/', ProductDetailsView.as_view(), name="product_details"),
    path('', HomePageView.as_view(), name="homepage"),
]
