from django.shortcuts import render
from reviews.models import Review
# Create your views here.


def HomePage(request):
    context = {}
    context['reviews'] = Review.objects.all().order_by('?')[:4]
    return render(request, 'main/index.html', context)
