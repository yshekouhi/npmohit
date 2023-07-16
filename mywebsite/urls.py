from django.contrib import admin
from django.urls import include, path

from django.conf.urls import (
handler400, handler403, handler404, handler500
)

from .views import AboutUsListView, ContactUsCreateView
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', AboutUsListView.as_view(), name="about"),
    path('contact_us/', ContactUsCreateView.as_view(), name="contact_us"),
    path('account/', include('account.urls'), name='account'),
    path('product/', include('product.urls'), name='product'),
    path('service/', include('service.urls'), name='service'),
    path('posts/', include('posts.urls'), name='posts'),
    path('checkout/', include('checkout.urls'), name='checkout'),
    path('pages/', include('pages.urls'), name='pages'),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),

]

handler404 = 'mywebsite.views.custom_page_not_found_view'
handler500 = 'mywebsite.views.custom_error_view'
handler403 = 'mywebsite.views.custom_permission_denied_view'
handler400 = 'mywebsite.views.custom_bad_request_view'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
admin.site.site_header = 'داشبورد نیک پاد محیط'
admin.site.site_title = 'نیک پاد محیط'
admin.site.index_title = 'مدیریت سایت'