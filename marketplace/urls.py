from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

from core.views import HomePageView
from product.views import ProductDetailsView

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('product/<slug:slug>/', ProductDetailsView.as_view(), name="product_details"),
    path('basket/', include('basket.urls')),
    path('shipment/', include('shipment.urls')),
    path('', HomePageView.as_view(), name="homepage"),
)

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
    urlpatterns += [path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})]
