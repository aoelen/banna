from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import HarvestForm
from farmer.models import Harvest

#SHOW OVERVIEW HARVEST
def overview_harvest(request, id=id):
    latest_harvest_list = Harvest.objects.all()
    context = {'latest_harvest_list': latest_harvest_list}
    return render(request, './overview/harvest.html', context)

#ADD HARVEST
def add_harvest(request):
    if request.method == "POST":
        form = Harvest(request.POST)
        if form.is_valid():
            harvest_item = form.save(commit=False)
            harvest_item.save()
            return redirect('/farmer/harvest')
    else:
        form = HarvestForm()
    return render(request, './add/harvest.html', {'harvest':form})

#EDIT HARVEST
def edit_harvest(request, id=None):
    item = get_object_or_404(Harvest, id=id)
    form = HarvestForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/farmer/harvest/')
    return render(request, './edit/harvest.html', {'harvest':form})


#DELETE HARVEST
def delete_harvest(request, id=id):
    harvest = Harvest.objects.get(pk=id) #get harvest which needed be deleted
    harvest.delete()
    return redirect('/farmer/harvest')