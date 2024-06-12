from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    context = {'form':form}
    return render(request, 'cad_reporting/index.html', context=context)
@login_required(login_url='login')
def home(request):
    return render(request,'cad_reporting/home.html')