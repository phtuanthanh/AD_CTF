from django.shortcuts import render, get_object_or_404

from .models import Flatpage

def flatpage(request, category=None, slug=''):
    return render(request, 'flatpage.html', status=200)
