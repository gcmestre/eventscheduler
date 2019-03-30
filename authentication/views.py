from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm


def signup_view(request):
    """
    Custom sign in page.
    Enables and anonymous User to sign in with Email and password
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username = form.cleaned_data.get('email')
            obj.first_name = obj.username.split('@')[0]
            obj.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})


def login_view(request):
    """
    Custom sign in page.
    Enables and anonymous User to  log in with Email and password
    """
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
    return render(request, 'authentication/login.html', {'form': LoginForm})