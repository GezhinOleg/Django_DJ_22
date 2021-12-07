from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    sort_method = request.GET.get('sort', 'name')
    phones = Phone.objects.order_by(sorting.get(sort_method))
    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
