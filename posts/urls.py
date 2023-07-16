from django.urls import path
from . import views
from .views import PostDetailView, PostListView

app_name = 'posts'
urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("<slug>/", PostDetailView.as_view(), name="detail"),
]

