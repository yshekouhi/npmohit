from django.urls import path
from . import views
from .views import CategoryServiceListView, ServiceDetailView, CategoryServiceDetailView

app_name = 'service'
urlpatterns = [
    # path("", ServiceListView.as_view(), name="service_list"),
    path("", CategoryServiceListView.as_view(), name="service_list"),
    path("<slug>/", CategoryServiceDetailView.as_view(), name="category_detail"),
    path("detail/<slug>/", ServiceDetailView.as_view(), name="detail"),
]

