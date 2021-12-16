from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from reviews.models import Review
# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    reviews = Review.objects.filter(user=request.user)
    context = {
        'reviews': reviews
    }
    return render(request, 'business/dashboard.html', context)
