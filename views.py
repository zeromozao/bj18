# -*- coding: UTF-8 –*-
from django.http import HttpResponse

def index(request):
    return HttpResponse('index')