from django.shortcuts import render, redirect
from newsletter.forms import SubscriberForm


from django.core.mail import send_mail
# from django.conf import settings
from mywebsite import settings
from django.urls import reverse

from django.shortcuts import render, get_object_or_404
from newsletter.models import Subscriber
from newsletter.forms import SubscriberForm
from django.contrib import messages


def send_verification_email(subscriber):
    verification_url = reverse('newsletter:verify_email', kwargs={'token': str(subscriber.verification_token)})
    verification_link = f"{settings.BASE_DIR}{verification_url}"
    subject = 'Verify your email address'
    message = f'Please click the following link to verify your email address: {verification_link}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [subscriber.email])


def verify_email(request, token):
    subscriber = get_object_or_404(Subscriber, verification_token=token)
    subscriber.is_verified = True
    subscriber.save()
    return render(request, 'newsletter/verification_success.html')


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            send_verification_email(subscriber)
            messages.success(request, "درخواست اشتراک شما با وفقیت ثبت شد.")
            return render(request, 'index.html')
        else:
            messages.error(request, "خطایی رخ داده دوباره سعی کنید/")
            return redirect('index.html')
    else:
        return redirect('index.html')
        
    #     form = SubscriberForm()
    # return render(request, 'newsletter/subscribe.html', {'form': form})

