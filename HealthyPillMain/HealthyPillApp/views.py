from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def base(request):

    return render(request, "HealthyPillApp/Base.html")

def login(request):

    return render(request, "HealthyPillApp/login.html")

def home(request):
    
    return render(request, 'HealthyPillApp/home.html')

def calendario(request):

    return render(request, "HealthyPillApp/calendario.html")

def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'usuario {username} creado')
			return redirect ('calendario')

	else:
		form = UserRegisterForm()
	context  ={'form': form } 
	return render(request,'HealthyPillApp/Registrate.html', context)