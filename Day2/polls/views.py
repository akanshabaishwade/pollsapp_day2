from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def choice(request):
    data = Choice.objects.all()
    context = {
      'data': data
    }
    return render(request, 'home.html', context)