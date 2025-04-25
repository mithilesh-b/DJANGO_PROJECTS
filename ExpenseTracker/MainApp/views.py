from django.shortcuts import render, HttpResponse

def index (request):
    return render(request, 'index.html')

# Create your views here.
def dailyspend (request):
    return render (request, 'dailyspend.html')