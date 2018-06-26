from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import redirect
from farmer.models import Report, UserForm, Reports_Yield


def form_fertilizer(request, farm_id, year, month, report_id):
    if request.method == "POST":
        Report.objects.filter(id=report_id).update(fertilizer_amount=request.POST.get('fertilizer_kgs', ''),
                                                   fertilizer_used=request.POST.get('fertilizer_used', ''))

        return redirect('/farmer/'+ str(farm_id) + '/' + str(year) + '/' + str(month) + '/' + str(report_id) + "/succes/")

    report = Report.objects.get(id=report_id)
    report.fertilizer_used = report.fertilizer_used.lower()

    context = {
        'report': report,
        'report_id': report_id,
        'farm_id': farm_id,
        'year': year,
        'month': month,
    }

    return render(request, 'farmer/form/fertilizer.html', context)



# def login(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             login_item = form.save(commit=False)
#             login_item.save()
#             return redirect('/farmer/overview/')
#     else:
#         form = UserForm()
#     return render(request, 'farmer/login.html', {'login': form})
#
#     context = {
#
#     }
#
#     return render(request, 'farmer/login.html', context)
