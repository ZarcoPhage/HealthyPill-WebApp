from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EventForm, UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from datetime import datetime, timedelta, date
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse 
from .models import *
from .utils import Calendario as C
#from .utils import reminder as R
from .forms import EventForm
from calendar import *
from django.contrib.auth.mixins import LoginRequiredMixin

def perfil(request):

    return render(request, "HealthyPillApp/Perfil.html")
def base(request):

    return render(request, "HealthyPillApp/Base.html")

def login(request):

    return render(request, "HealthyPillApp/login.html")

def home(request):
    
    return render(request, 'HealthyPillApp/home.html')

def calendario(request):

    return render(request, "HealthyPillApp/calendario.html")

def especialistas(request):
    users = UserProfile.objects.all()

    return render(request, "HealthyPillApp/ContactosEspecialistas.html", {'users' : users})

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

class CalendarView(LoginRequiredMixin,generic.ListView):
    model = Event
    template_name = 'HealthyPillApp/calendario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = C(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal) 
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return HttpResponseRedirect(reverse('calendario'))
    return render(request, 'HealthyPillApp/event.html', {'form': form})