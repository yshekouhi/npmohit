
from django.urls import path
from .views import ProductCreateView, ProductDetailView, ProductUpdateView, CategoryDetailView, ProductCategoryListView
from . import views

app_name = 'product'
urlpatterns = [
    path("categories/", ProductCategoryListView.as_view(), name="index"),
    path("category/<slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('<slug:slug>/update/', ProductUpdateView.as_view(), name="update"),
    path('search/', views.search_view, name="search"),
    path('<slug>/', ProductDetailView.as_view(), name="detail"),
]

