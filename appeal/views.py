from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Appeal
from .forms import AppealForm


def appeal(request):
    return render(request, 'appeal/appeal.html')

def appeal_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    	form = AppealForm(request.POST)
    	print(form)
    	if form.is_valid():
    		appeal = Appeal()
    		appeal.appeal_num         = form.cleaned_data['appeal_num']
    		appeal.bsk_number         = form.cleaned_data['bsk_number']
    		appeal.appeal_create_date = form.cleaned_data['appeal_create_date']
    		appeal.appeal_owner_name  = form.cleaned_data['appeal_owner_name']
    		appeal.save()
    		return HttpResponseRedirect('/appeal/appeal_create')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppealForm()

    return render(request, 'appeal/create.html', {'form': form})

def appeal_list(request):
    context = Appeal.objects.all()
    return render(request, 'appeal/list.html', {'context': context})

def appeal_detail(request, appeal_id):
    return render(request, 'appeal/list.html')