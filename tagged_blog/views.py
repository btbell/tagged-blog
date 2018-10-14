from django.shortcuts import render
from django.http import HttpResponse
from django import template

import datetime

# Create your views here.

def index(request):
    return HttpResponse("hello django!")

def time(request):
    now = datetime.datetime.now()
    t = template.Template("<html><body>Current date and time {{ now }}</body></html>")
    c = template.Context({'now': now})
    html = t.render(c)
    return HttpResponse(html)