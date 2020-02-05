from django.shortcuts import render
from Feed.models import Rcp
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def details(request, R_name, U_name):
    obj = Rcp.objects.get(uname=U_name, Rname = R_name)
    return render(request, 'details.html', {'context' : obj})