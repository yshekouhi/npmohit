from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class CategoryService(models.Model):
    title = models.CharField(_("عنوان"), max_length=150)
    order = models.IntegerField(_("ترتیب"), null=True, blank=True)
    display = models.BooleanField(_("نمایش داده شود؟"), default=True)
    description = models.TextField(_("توضیحات"))
    slug = models.SlugField(_("اسلاگ"),allow_unicode=True) 
    icon = models.CharField(_("آیکون"), max_length=50, default='bi bi-toggles2')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("service:category_list", args={self.slug})    
    
    class Meta:
        verbose_name = 'دسته‌بندی خدمت'
        verbose_name_plural = 'دسته‌بندی خدمات'  


# Create your models here.
class Item(models.Model):
    category = models.ForeignKey(CategoryService, verbose_name=_("گروه"), on_delete=models.CASCADE, related_name='items')
    title = models.CharField(_("عنوان"), max_length=150)
    description = models.TextField(_("توضیحات"))
    image = models.ImageField(_("تصویر"), upload_to='service/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(_("اسلاگ"),allow_unicode=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("service:detail", args={self.slug})    
    
    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'          