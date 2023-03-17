from django.shortcuts import render

# Create your views here.
def grape(request):
    return render(request,'grape.html')