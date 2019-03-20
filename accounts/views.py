from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import registration_activation_token
from django.core.mail import EmailMessage

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username=request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already used for another account.')
                return redirect('home')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is already used by another account.")
                    return redirect('home')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    user.is_active = True
                    user.save()
                    login(request, user)
                    # current_site = get_current_site(request)
                    # mail_subject = 'Activate your blog account'
                    # message = render_to_string('accounts/activate_registration.html', {
                    #     'user': user,
                    #     'domain': current_site.domain,
                    #     'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    #     'token': registration_activation_token.make_token(user)
                    # })
                    # to_email = email
                    # email_body = EmailMessage(
                    #     mail_subject, message, to=[to_email]
                    # )
                    # email_body.send()
                    # print(user.username)
                    messages.success(request, "You are now registered and logged in. Welcome!")
                    return redirect('home')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('home')

    return redirect('home')

def activate_registration(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and registration_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Your registrtion is complete. Your are now logged in. Welcome')
        # return redirect('home')
        return redirect('home')
    else:
        messages.error(request, 'Sorry. Your activation token is invalid. Please register again!')
        return redirect('home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Your password or username or both are incorrect!')
            return redirect('login')

    return redirect('home')

def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('home')

