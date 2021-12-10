from datetime import datetime, timedelta
from calendar import HTMLCalendar

from django.contrib.auth.signals import user_logged_in
from django.http.request import HttpRequest
from .models import Event, UserProfile
from django.http import request
from django.contrib.auth.models import User

class Calendario(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendario, self).__init__()

	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		usersList = UserProfile.objects.all()
		for event in events_per_day:
			for user in usersList:
				userName = user.username
				eventuser = event.user.username
				print (userName)
				print(User.is_authenticated)
				print(event.user.username)
				if userName == eventuser:
					print("PASSED")
					if User.is_authenticated:
						d += f'<li> {event.get_html_url} </li>'
				else: 
					print("NOT PASSED")	
					

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
'''
class reminder():
	def __init__(self):
		pass
	
	def formatday(self, day, events):
		allEvents = Event.objects.all()
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			if User.is_authenticated:
				#if User.username == event.user:
				d += f'<li> {event.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'	
'''