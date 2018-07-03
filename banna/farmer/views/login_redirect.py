from django.shortcuts import redirect

def login_redirect(request):
    #set default language to english
    language_code = 'en'
    request.session['language_code'] = language_code

    #if user is part of the governemnt or factory
    if (request.user.groups.filter(name='government').exists() or request.user.groups.filter(name='factory').exists()):
        return redirect('/dashboard/overview')

    #if user is a farmer
    elif (request.user.groups.filter(name='farmer').exists()):
        return redirect('/farmer/language/')

    #go to login page
    else:
        return redirect('/login')
