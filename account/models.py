from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not username:
            raise ValueError(_("کاربر باید نام کاربری داشته باشد."))
        
        if not email:
            raise ValueError(_("کاربر باید آدرس ایمیل داشته باشد."))
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superadmin = True
        user.is_active = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    first_name = models.CharField(_("نام"), max_length=50)
    last_name = models.CharField(_("نام خانوادگی"), max_length=50)
    username = models.CharField(_("نام کاربری"), max_length=50, unique=True)
    email = models.EmailField(_("ایمیل"), max_length=254, unique=True)
    phone_number = models.CharField(_("تلفن"), max_length=50)

    date_joined = models.DateTimeField(_("تاریخ عضویت"), auto_now=False, auto_now_add=True)
    last_login = models.DateTimeField(_("آخرین ورود"), auto_now=True, auto_now_add=False)

    is_admin = models.BooleanField(_("ادمین؟"), default=False)
    is_active = models.BooleanField(_("فعال؟"), default=False)
    is_staff = models.BooleanField(_("کارمند؟"), default=False)
    is_superadmin = models.BooleanField(_("ادمین اصلی؟"), default=False)

    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obg=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    def get_full_name(self):
        return f'{ self.first_name } {self.last_name }'

    class Meta:
        verbose_name_plural = "کاربران"
        verbose_name = "کاربر"  
