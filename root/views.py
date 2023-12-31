from django.shortcuts import render
from .models import Services


def home(request):
    services = Services.objects.filter(status=True)[:3]
    context = {
        'services': Services
    }
    return render(request,'root/index.html',context=context)

def about(request):
    return render(request,'root/about.html')

def contact(request):
    return render(request,'root/contact.html')
