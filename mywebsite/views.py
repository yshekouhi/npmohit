from django.shortcuts import render
from product.models import Product
from pages.forms import ContactUsForm
from service.models import CategoryService
from pages.models import AboutUs, ContactUs
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


def index(request):
    category_service = CategoryService.objects.filter(display=True).order_by('order')
    products = Product.objects.all()
    context = {
        'products': products,
        'category_service': category_service
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


class AboutUsListView(ListView):
    model = AboutUs
    template_name = "pages/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] =  AboutUs.objects.filter(display=True).first()
        return context
    
    context_object_name = 'about'

class ContactUsCreateView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    success_url = '/'    
    template_name = 'pages/contact_us.html'
    success_message = "پیام شما با موفقیت ثبت شد."


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})