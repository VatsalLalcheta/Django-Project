from django.shortcuts import render
from Feed.models import Rcp
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def profile(request):
    match = Rcp.objects.filter(uname=request.user)
    return render(request, 'profiile.html', {'context' : match})