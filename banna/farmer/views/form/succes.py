from django.shortcuts import get_object_or_404, render, redirect

def success(request, farm_id, year, month, report_id):

    context = {
        'report_id': report_id,
        'farm_id': farm_id,
        'year': year,
        'month': month,
    }

    return render(request, 'farmer/form/success.html', context)