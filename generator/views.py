from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html', {'password':'heypass'})

def password(request):
    
    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('specialchar'):
        character.extend(list('!@#$%^&*()'))

    if request.GET.get('number'):
        character.extend(list('0123456789'))

    len = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(len):
        thepassword +=random.choice(character)

    return render(request,'generator/password.html', {'password': thepassword})

def about(request):
    return render(request,'generator/About Me.html')
