from django.db import models
from django.urls import reverse
from account.models import User
from django.utils.translation import gettext as _

    
# Create your models here.
class CustomProduct(models.Model):
    user = models.ForeignKey(User, verbose_name=_("متقاضی"), on_delete=models.CASCADE)
    title = models.CharField(_("عنوان"), max_length=150)
    description = models.TextField(_("توضیحات"))
    files = models.FileField(_("بارگذاری فایل"), upload_to='requests/', null=True, blank=True)
    status = models.BooleanField(_("تایید درخواست"), default=False)
    reply = models.TextField(_("پاسخ"), blank=True, null=True)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("product:category_detail", args={self.slug})    
    
    class Meta:
        verbose_name = 'درخواست'
        verbose_name_plural = 'درخواست‌ها'  


class ContactUs(models.Model):
    class Title(models.TextChoices):
        RECOMMENT = "پیشنهاد", _("پیشنهاد")
        CRITIC = "CRITIC", _("انتقاد")
        FOLLOW = "FOLLOW", _("پیگیری")
        OTHER = "OTHER", _("سایر موضوعات")
   
    full_name = models.CharField(_("نام"), max_length=100)
    title = models.CharField(_("عنوان"), max_length=150, choices=Title.choices)
    email = models.EmailField(_("آدرس ایمیل"), max_length=50)
    phone_number = models.CharField(_("شماره تماس"), max_length=20)
    description = models.TextField(_("متن پیام"))

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام‌ها'  

class AboutUs(models.Model):
    title = models.CharField(_("عنوان"), max_length=100)
    body = models.TextField(_("متن پیام"))
    display = models.BooleanField(_("نمایش داده شود؟"), default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباه ما'
