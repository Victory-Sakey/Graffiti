from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def sts(request):
    return render(request, 'sts.html')
