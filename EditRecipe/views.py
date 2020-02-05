from django.shortcuts import render, redirect
from Feed.models import Rcp
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def edit(request, R_name):
    uname = request.user
    if request.method=='POST':
        print(R_name)
        Rname = request.POST['R_name']
        Ingredients = request.POST['Ingredients']
        steps = request.POST['steps']
        obj = Rcp.objects.filter(uname=uname, Rname=R_name).update(Rname=Rname, Ingredients=Ingredients, steps=steps)
        return redirect('/profile_page/profile')

    obj = Rcp.objects.get(uname=uname, Rname = R_name)
    return render(request, 'edit.html', {'context' : obj})