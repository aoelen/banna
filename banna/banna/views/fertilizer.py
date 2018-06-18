from django.shortcuts import get_object_or_404, render, redirect

from ..models.modalforms import FertilizerForm
from ..models.models import Fertilizer

#SHOW OVERVIEW FERTILIZER
def overview_fertilizers(request, id=id):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, '/overview/fertilizers.html', context)


#ADD FERTILIZER
def add_fertilizer(request):
    if request.method == "POST":
        form = Fertilizer(request.POST)
        if form.is_valid():
            fertilizer_item = form.save(commit=False)
            fertilizer_item.save()
            return redirect('overview/fertilizers')
    else:
        form = FertilizerForm()
    return render(request, '/add/fertilizer.html', {'fertilizer':form})

#EDIT FERTILIZER
def edit_fertilizer(request, id=None):
    item = get_object_or_404(Fertilizer, id=id)
    form = FertilizerForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/fertilizer/')
    return render(request, '/edit/fertilizer.html', {'fertilizer':form})


#DELETE FERTILIZER
def delete_fertilizer(request, id=id):
    fertilizer = Fertilizer.objects.get(pk=id) #get fertilizer which needed be deleted
    fertilizer.delete()
    return redirect('overview/fertilizers')