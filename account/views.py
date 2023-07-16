from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User

from django.contrib import auth, messages

# User account verification
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage




# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name  = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            email  = form.cleaned_data['email']
            phone_number  = form.cleaned_data['phone_number']
            password  = form.cleaned_data['password']
            username = email.split('@')[0]

            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email ,
                password  = password ,
                username  = username ,
            )
            user.phone_number = phone_number
            user.save()

            current_site = get_current_site(request)
            mail_subject = "Please activate your account"
            message = render_to_string('account/verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })

            to_email = email
            msg = EmailMessage(mail_subject, message, to=[to_email])
            msg.send()

            # messages.success(request, 'Thank you for registration.')
            command = 'verification'
            return redirect('/account/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()

    context = { 'form': form }
    return render(request, 'account/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST': 
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        next = request.POST['next']
        if user is not None:
            auth.login(request, user)
            if next:
                return redirect(next)
            return redirect('/')
        else:
            messages.warning(request, "اطلاعات وارد شده صحیح نیست")
    return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    user = auth.get_user(request)
    return render(request, 'account/profile.html', {'user': user} )


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "حساب کاربری شما با موفقیت فعالسازی شد.")
        return redirect('account:login')
    else:
        messages.error(request, "فعالسازی ناموفق حساب کاربری")
        return redirect('account:register')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            current_site = get_current_site(request)
            mail_subject = "Please reset your password"
            message = render_to_string('account/forgot_activate_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })

            to_email = email
            msg = EmailMessage(mail_subject, message, to=[to_email])
            msg.send()
            messages.success(request, "لینک تغییر رمز عبور به آدرس ایمیل شما ارسال شد.") 
            return redirect('account:login')
        else:
            messages.error(request, "حساب کاربری [ "+ email +" ] وجود ندارد") 
            return redirect('account:forgot_password')

    return render(request, 'account/forgot_password.html')


def password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token): 
        request.session['uid'] = uid
        messages.success(request, "لطفا رمز عبور خود را بازنشانی کنید")
        return redirect('account:reset_password')
    else:
        messages.error(request, "مهلت استفاده از این لینک به پایان رسیده است.")
        return redirect('account:login')   
    

def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, "بازنشانی رمز عبور با موفقیت انجام شد.")
            return redirect('account:login')
        else:
            messages.error(request, "رمز عبور سازگار نیست")
            return redirect('account:reset_password')
    else:
        return render(request, 'account/reset_password.html')
    

