from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpResponse
from farmer.models import Month, Farm, Report, UserForm, Reports_Yield

def index(request):
    return HttpResponse("<h2>You are at the farmer page!</h2>")

def overview(request):

    context = {

    }

    return render(request, 'farmer/overview.html', context)


def form_planted(request):

    context = {

    }

    return render(request, 'farmer/form_planted.html', context)


def form_harvest(request):

    context = {

    }

    return render(request, 'farmer/form_harvest.html', context)


def form_fertilizer(request):

    context = {

    }

    return render(request, 'farmer/form_fertilizer.html', context)


def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            login_item = form.save(commit=False)
            login_item.save()
            return redirect('/farmer/overview/')
    else:
        form = UserForm()
    return render(request, 'farmer/login.html', {'login': form})

    context = {

    }

    return render(request, 'farmer/login.html', context)
