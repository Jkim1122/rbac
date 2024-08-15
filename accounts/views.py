from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#Home View
def home(request):
    return render(request, 'home.html')

#Signup Views:
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')
        else:
            return redirect('signup_failure')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def signup_success(request):
    return render(request, 'accounts/signup_success.html')

def signup_failure(request):
    return render(request, 'accounts/signup_failure.html')

#Login View:
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
            
#Logout View:
def logout_view(request):
    logout(request)
    return redirect('login')
