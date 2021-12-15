from django.shortcuts import render
from catergory.models import Catergory
from reviews.models import Review
# Create your views here.


def HomePage(request):
    context = {}
    context['reviews'] = Review.objects.all().order_by('?')[:4]
    context['catergories'] = Catergory.objects.all().order_by('?')[:6]
    return render(request, 'main/index.html', context)
