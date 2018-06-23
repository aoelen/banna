# from django.shortcuts import get_object_or_404, render, redirect
#
# from farmer.models import HarvestForm
# from farmer.models import Harvest
#
#
# #SHOW OVERVIEW DATA MONTH
# def overview_month(request, id=id):
#     latest_month_list = Harvest.objects.all()
#     context = {'latest_month_list': latest_month_list}
#     return render(request, './overview.html', context)
#
# #ADD HARVEST
# def add_harvest(request, id=id):
#     month = Harvest.objects.month()
#     if request.method == "POST":
#         form = Harvest(request.POST)
#         if form.is_valid():
#             harvest_item = form.save(commit=False)
#             harvest_item.save()
#             return redirect('/farmer/harvest')
#     else:
#         form = HarvestForm()
#     return render(request, 'form_harvest.html', {'harvest':form})
#
# #EDIT HARVEST
# def edit_harvest(request, id=None):
#     item = get_object_or_404(Harvest, id=id)
#     form = HarvestForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('/farmer/harvest/')
#     return render(request, './form_harvest.html', {'harvest':form})