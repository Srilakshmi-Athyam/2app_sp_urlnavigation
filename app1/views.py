from django.shortcuts import render

# Create your views here.
def mango(request):
    return render(request,'mango.html')