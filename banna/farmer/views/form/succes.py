from django.shortcuts import get_object_or_404, render, redirect
from farmer.models import Report
from datetime import datetime, date

def success(request, farm_id, year, month, report_id):
    Report.objects.filter(id=report_id).update(report_date=datetime.now().date())

    context = {
        'report_id': report_id,
        'farm_id': farm_id,
        'year': year,
        'month': month,
    }

    return render(request, 'farmer/form/success.html', context)