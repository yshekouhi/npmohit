from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class Post(models.Model):
    author = models.CharField(_("نویسنده"), max_length=50, default='')
    title = models.CharField(_("عنوان"), max_length=150)
    slug = models.SlugField(_("اسلاگ"),allow_unicode=True)
    intro = models.TextField(_("خلاصه"))
    body = models.TextField(_("متن"))
    image = models.ImageField(_("تصویر"), upload_to='posts/', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("تاریخ ویرایش"), auto_now=True, auto_now_add=False)
    featured = models.BooleanField(_("مطلب ویژه"), default=False)
    top_post = models.BooleanField(_("مطلب اصلی"), default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", args={self.slug})    
    
    class Meta:
        verbose_name = 'مطلب'
        verbose_name_plural = 'مطالب'          