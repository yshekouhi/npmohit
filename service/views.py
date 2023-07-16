from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Item, CategoryService

class ServiceDetailView(DetailView):
    template_name = 'service/detail.html'
    model = Item 

class CategoryServiceDetailView(DetailView):
    template_name = 'service/category_detail.html'
    model = CategoryService 

class CategoryServiceListView(ListView):
    template_name = 'service/service_list.html'
    model = CategoryService
    ordering = ['order']