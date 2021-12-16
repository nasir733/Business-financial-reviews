from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from reviews.models import Review
# Create your views here.


@login_required(login_url='login')
def index(request):
    context = {}
    context['reviews'] = Review.objects.filter(user=request.user)
    context['user'] = request.user
    return render(request, 'dashboard/user-dashboard.html', context)


@login_required(login_url='login')
def EditProfile(request):
    context = {}
    context['reviews'] = Review.objects.filter(user=request.user)
    context['user'] = request.user
    if request.method == 'POST' or request.method == "FILES":
        print('POST')
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        profile_pic = request.FILES.get('profile_pic')

        if profile_pic is None:
            print('No file')
        else:
            user.profile_pic = profile_pic
        user.save()
        return redirect('dashboard')
    return render(request, 'dashboard/user-settings.html', context)
