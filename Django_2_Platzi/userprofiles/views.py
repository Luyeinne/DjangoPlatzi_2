from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.filter(username=username).first()
            if user:
                error_message_signup = "This user already exists. Please try again."
                return render(
                    request,
                    'login.html',
                    {"error_signup": error_message_signup }
                    )
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
            )
            print(user)
            user.save()
            message_user_created = "user created successfully, now log in"
            return render(
                    request,
                    'login.html',
                    {"user_created": message_user_created }
                    )

        elif action == 'login':
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_message = "Invalid username or password. Please try again."
                return render(
                    request,
                    'login.html',
                    {"error_login": error_message }
                )

    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)

    return redirect('/login')

