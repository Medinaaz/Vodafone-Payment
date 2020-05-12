from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from product.models import ProductCategory, Product
from django.template import loader
import random

class IndexView(generic.ListView):
    template_name = 'listing/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        sample_entities = Product.objects.all()[:4]
        return sample_entities

#List products
def product_list(request, slug):
    if slug[:6] == 'search':
        return search(request)
        
    products = Product.objects.filter(category__slug = slug)
    context = {'products': products, "category": slug}
    #context = {'products': products, "category": slug, "categories": ProductCategory.objects.values_list('slug')}
    return render(request, 'listing/product_list.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    slug = request.GET["category"]
    products = Product.objects.filter(
        category__slug=slug)
    
    min_price = request.GET.get('min-price')
    if is_valid_queryparam(min_price):
        products = products.filter(price__gte  =  min_price)
        
    max_price = request.GET.get('max-price')
    if is_valid_queryparam(max_price):
        products = products.filter(price__lte  =  max_price)
    
    
    price_and_category_filtered = products
    
    brand_vodafone = request.GET.get('Vodafone')
    brand_samsung = request.GET.get('Samsung')
    brand_iphone = request.GET.get('Iphone')
    brand_huawei = request.GET.get('Huawei')
    brand_xiaomi = request.GET.get('Xiomi')
    
    
    all_products = []
    flag = True
    if brand_vodafone == 'on':
        products = price_and_category_filtered.filter(description__icontains="Vodafone")
        all_products += products
        flag = False
    if brand_iphone == 'on':
        products = price_and_category_filtered.filter(description__icontains="Iphone")
        all_products += products
        flag = False
    if brand_samsung == 'on':
        products = price_and_category_filtered.filter(description__icontains="Samsung")
        all_products += products
        flag = False
    if brand_xiaomi == 'on':
        products = price_and_category_filtered.filter(description__icontains="Xiaomi")
        all_products += products
        flag = False
    if brand_huawei == 'on':
        products = price_and_category_filtered.filter(description__icontains="Huawei")
        all_products += products
        flag = False
    
    
    context = {'products': price_and_category_filtered if flag else all_products, "category": slug}
    return render(request, 'listing/product_list.html', context)

def search(request):
    searchText = request.GET['searchText']
    allProducts = Product.objects.all()
    foundProducts = []
    for product in allProducts:
        if(searchText.lower() in product.name.lower()):
            foundProducts.append(product)
    
    context = {'products': foundProducts}
    return render(request, 'listing/product_list.html', context)
