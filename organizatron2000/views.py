from django.http import HttpResponseRedirect
from django.shortcuts import render



def dashboard(request):
    # if this is a POST request we need to process the form data
    return render(request, 'main.html')

