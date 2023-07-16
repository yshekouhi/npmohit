from django.db import models
from django.urls import reverse
from .storage import ProtectedMedia
from django.utils.translation import gettext as _


# Create your models here.
class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=150)
    description = models.TextField(_("توضیحات"))
    slug = models.SlugField(_("اسلاگ"),allow_unicode=True)
    image = models.ImageField(_("تصویر"), upload_to='category/image', height_field=None, width_field=None, max_length=None) 
    timestamp = models.DateTimeField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("تاریخ به روزرسانی"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product:category_detail", args={self.slug})    
    
    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'        
    

    def download_media(instance, filename):
        return "%s/%s"%(instance.slug, filename)


class Product(models.Model):
    user = models.ForeignKey("account.User", verbose_name=_("کاربر"), on_delete=models.CASCADE)
    title = models.CharField(_("عنوان"), max_length=150)
    category = models.ForeignKey(Category , verbose_name=_("دسته‌بندی"), on_delete=models.CASCADE)
    slug = models.SlugField(_("اسلاگ"), unique=True , allow_unicode=True)
    image = models.ImageField(_("تصویر"), upload_to='product/image', null=True, blank=True)
    media = models.FileField(_("رسانه"), upload_to='download_media', storage=ProtectedMedia, null=True, blank=True)
    description = models.TextField(_("توضیحات"), null=True, blank=True)
    price = models.IntegerField(_("قیمت"))
    unit = models.CharField(_("واحد"), max_length=150)
    featured = models.BooleanField(_("محصول ویژه؟"), default=False)
    recent_product = models.BooleanField(_("محصول جدید؟"), default=False)
    available = models.BooleanField(_("موجود است؟"))

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product:detail", args={self.slug})
    
    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"
    
class Specifications(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE)
    title = models.CharField(_("مشخصه"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=50)

    class Meta:
        verbose_name_plural = "مشخصات محصول"
        verbose_name = "مشخصه "   


     
 