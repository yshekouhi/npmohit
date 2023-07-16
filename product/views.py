from django.http import HttpResponse
from django.shortcuts import render
from itertools import chain
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, Category
from .forms import ProductForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.db.models import Q
from django.core.paginator import Paginator
from checkout.models import CartItem
from checkout.views import cart_id


# Create your views here.
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create_view.html'
    success_url = '/'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update_view.html'
    success_url = '/'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        related_products = Product.objects.filter(category=product.category).exclude(slug=product.slug)
        # is_in_cart = CartItem.objects.all().filter(cart__cart_id=cart_id(self.request), product=product).exists()
        context["related_products"] = related_products
        # context["is_in_cart"] = is_in_cart
        return context

def search_view(request, *args, **kwargs):
    try:
        q = request.GET.get('q',)
    except:
        q = False
    if q== None:
        return render(request, 'product/search_result.html')        
    obj = Product.objects.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(category__title__icontains=q))
    results = list(chain(obj))
    paginator = Paginator(results, 1)
    page = request.GET.get('page')
    page_products = paginator.get_page(page)
    context = {
        'results': page_products,
        'obj': obj,
        'q': q
    }
    return render(request, 'product/search_result.html', context)


class ProductCategoryListView(ListView):
    template_name = 'product/category_list.html'
    model = Category
    paginate_by = 5

    

class CategoryDetailView(DetailView):
    model = Category

    template_name = 'product/category_detail.html'
    
    def get_context_data(self, **kwargs):
        id = self.get_object().id
        context = super().get_context_data(**kwargs)
        context["products"] =  Product.objects.filter(category__pk=id)
        return context    


    
    