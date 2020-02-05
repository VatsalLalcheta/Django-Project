from django.shortcuts import render, redirect
from .models import Rcp
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def feed(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    context = Rcp.objects.all()
    return render(request, 'Feed.html', {'context' : context})


def add(request):
    if request.method == 'POST':
        username = request.user.username
        Rname = request.POST['R_name']
        Ingredients = request.POST['Ingredients']
        image = 'Rcp_Images/' + request.POST['img']
        steps = request.POST['steps']
        p = Rcp(uname = username, Rname = Rname, Ingredients=Ingredients, image=image, steps = steps)
        p.save()
        print('saved successfully')
        return render(request, 'add.html')
    else:
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        return render(request, 'add.html')


def search(request):
    if request.method == 'POST':
        srch = request.POST['search_box']

        if srch:
            match = Rcp.objects.filter(Q(Rname__icontains=srch) | Q(Ingredients__icontains=srch))

            if match:
                return render(request, 'search.html', {'sr' : match})

            else:
                messages.error(request, 'No results Found')
        else:
            return render(request, 'search.html')
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    return render(request, 'search.html')
