from django.shortcuts import render
 

def index(request):
    data = {
        'title': 'Main Page)',
        'values': ['First', 'Second', 'Third'],
        'obj' : {
            'car':'BMW',
            'age': 10,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
