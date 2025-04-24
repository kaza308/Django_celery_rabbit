from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .tasks import add


def index(request):
    add.delay(2,3)
    return HttpResponse('OK')

