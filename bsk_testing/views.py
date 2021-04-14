from django.shortcuts import render

# Create your views here.
def bsk_testing(request):
	return render(request, 'bsk_testing/bsk_testing.html')