from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): 

    return render(request, 'lmsreporting/home.html', {'title': 'Welcome'})

def about(request): 

    return render(request, 'lmsreporting/about.html', {'title': 'About'})


def contact(request): 

    return render(request, 'lmsreporting/contact.html', {'title': 'Contact'})


def modules(request): 

    return render(request, 'lmsreporting/modules.html', {'title': 'Modules'})
