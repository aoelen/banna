from django.shortcuts import redirect

def login_redirect(request):
    language_code = 'en'
    request.session['language_code'] = language_code

    if (request.user.groups.filter(name='government').exists() or request.user.groups.filter(name='factory').exists()):
        return redirect('/dashboard/overview')
    elif (request.user.groups.filter(name='farmer').exists()):
        return redirect('/farmer/language/')
    else:
        return redirect('/login')
