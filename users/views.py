from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import get_user_model

from django.contrib.auth import logout as django_logout
from catergory.models import Catergory
from companydashboard.models import BusinessProfile
User = get_user_model()


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            username = User.objects.get(email=email.lower()).username
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')
        else:
            return redirect('login')
    return render(request, 'users/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']

        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')
    return render(request, 'users/register.html')


def businessregister(request):
    if request.method == 'POST' or request.method == 'FILES':
        business_name = request.POST['business_name']
        business_email = request.POST['business_email']
        catergory_id = int(request.POST['catergory'])
        image = request.FILES['image']

        catergory = Catergory.objects.get(id=catergory_id)
        user = request.user

        BusinessProfile.objects.create(
            user=user, name=business_name, email=business_email, catergory=catergory, image=image)
        return redirect('business:dashboard', name=business_name, page=1)

    return render(request, 'users/business-register.html')


@login_required(login_url='login')
def logout(request):
    django_logout(request)
    print('the user is logged out')
    return redirect('/')
