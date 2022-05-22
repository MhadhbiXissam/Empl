from django.shortcuts import render
from django.http import HttpResponse
import os

def homepage(request) : 
	return HttpResponse(open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'index.html')).read())

def addnewempl(request) : 
	return HttpResponse(open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'new_empl.html')).read())