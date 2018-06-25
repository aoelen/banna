from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    # Render the .html file
    return render(request, 'dashboard/dashboard.html')

def login(request):

    # Render the .html file
    return render(request, 'dashboard/login.html')

def dashboard(request):

    # Render the .html file
    return render(request, 'dashboard/dashboard.html')

def add_farmer(request):

    # Render the .html file
    return render(request, 'dashboard/add_farmer.html')

def add_user(request):

    # Render the .html file
    return render(request, 'dashboard/add_user.html')

def edit_farmer(request):

    # Render the .html file
    return render(request, 'dashboard/edit_farmer.html')

def factory_data(request):

    # Render the .html file
    return render(request, 'dashboard/factory_data.html')

def factory_overview(request):

    # Render the .html file
    return render(request, 'dashboard/factory_overview.html')

def factory(request):

    # Render the .html file
    return render(request, 'dashboard/factory.html')

def farmers(request):

    # Render the .html file
    return render(request, 'dashboard/farmers.html')

def harvests(request):

    # Render the .html file
    return render(request, 'dashboard/harvests.html')

def trees(request):

    # Render the .html file
    return render(request, 'dashboard/trees.html')

def users(request):

    # Render the .html file
    return render(request, 'dashboard/users.html')
