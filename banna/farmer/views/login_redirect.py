from django.shortcuts import redirect

def login_redirect(request):
    if (request.user.groups.filter(name='government').exists() or request.user.groups.filter(name='factory').exists()):
        return redirect('/dashboard/dashboard')
    elif (request.user.groups.filter(name='farmer').exists()):
        return redirect('/farmer/language/')
    else:
        return redirect('/login')
