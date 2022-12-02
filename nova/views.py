from django.shortcuts import render

# Create your views here.

def nova_home(request):
    return render(request, 'nova/nova_home.html' )