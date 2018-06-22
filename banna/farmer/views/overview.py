from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Month

#SHOW OVERVIEW DATA MONTH
def overview_month(request, id=id):
    latest_month_list = Month.objects.all()
    print(latest_month_list)
    context = {'latest_month_list': latest_month_list}
    return render(request, './overview.html', context)