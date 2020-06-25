from django.shortcuts import render
from django.http import HttpResponse

def homepage(requests):
	return render( requests, 'homepage/index.html')

def services(requests):
	return render(requests, 'homepage/services.html')

def portfolio(requests):
	return render(requests, 'homepage/portfolio.html')

