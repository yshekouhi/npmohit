from django.shortcuts import render
from .models import CustomProduct
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CustomProductForm, ContactUsForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin



@method_decorator(login_required, name='dispatch')
class CustomProductCreateView(LoginRequiredMixin, CreateView):
    model = CustomProduct
    form_class = CustomProductForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["custom_products"] = CustomProduct.objects.filter(user=self.request.user)
        return context
    
    template_name = 'pages/custom_product_request.html'
    success_url = '/'
    success_message = "درخواست شما با موفقیت ثبت شد. از قسمت پروفایل میتوانید درخواست را پیگیری کنید."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

