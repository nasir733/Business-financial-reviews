from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from reviews.models import Review
# Create your views here.
from catergory.models import Catergory
from companydashboard.models import BusinessProfile
from reviews.models import Review
from django.db.models import Avg

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage


@login_required(login_url='login')
def dashboard(request, name, page=1):
    context = {}

    business_id = BusinessProfile.objects.filter(
        name=name, user=request.user).first().id
    reviews = Review.objects.filter(business__id=business_id)
    context['reviews_count'] = reviews.count()
    paginator = Paginator(reviews, 10)
    context['business'] = BusinessProfile.objects.get(id=business_id)
    try:

        context['reviews'] = paginator.page(page)
    except EmptyPage:
        # if we exceed the page limit we return the last page
        context['reviews'] = paginator.page(paginator.num_pages)
    context['avg_rating'] = Review.objects.filter(
        business__id=business_id).aggregate(Avg('rating'))
    five_star = Review.objects.filter(business__id=business_id, rating=5)
    four_star = Review.objects.filter(business__id=business_id, rating=4)
    three_star = Review.objects.filter(business__id=business_id, rating=3)
    two_star = Review.objects.filter(business__id=business_id, rating=2)
    one_star = Review.objects.filter(business__id=business_id, rating=1)

    if len(context['reviews']) > 0:
        context['five_star'] = len(five_star)/len(context['reviews']) * 100
        context['four_star'] = len(four_star)/len(context['reviews'])*100
        context['three_star'] = len(three_star)/len(context['reviews'])*100
        context['two_star'] = len(two_star)/len(context['reviews'])*100
        context['one_star'] = len(one_star)/len(context['reviews'])*100
    else:
        context['five_star'] = 0
        context['four_star'] = 0
        context['three_star'] = 0
        context['two_star'] = 0
        context['one_star'] = 0
    return render(request, 'business/dashboard.html', context)


@ login_required(login_url='login')
def EditProfile(request, name):
    context = {}
    context['reviews'] = Review.objects.filter(user=request.user)
    context['business'] = BusinessProfile.objects.filter(
        name=name, user=request.user).first()
    context['user'] = request.user
    if request.method == 'POST' or request.method == "FILES":
        print(request.POST)
        user = request.user
        business = BusinessProfile.objects.get(name=name, user=user)
        user.username = request.POST['username']
        user.email = request.POST['email']
        business.name = request.POST['business_name']
        business.email = request.POST['business_email']
        business.description = request.POST['description']
        business.address = request.POST['address']
        business.phone = request.POST['phone']
        business.website = request.POST['website']
        business.facebook = request.POST['facebook']
        business.twitter = request.POST['twitter']
        business.instagram = request.POST['instagram']
        if request.POST['catergory'] != "":
            catergory_id = int(request.POST['catergory'])
            business.catergory = Catergory.objects.get(id=catergory_id)
        image = request.FILES.get('image')

        if image is None:
            print('No file')
        else:
            business.image = image
        user.save()
        business.save()
        return redirect('business:dashboard', name=name, page=1)
    return render(request, 'business/user-settings.html', context)


@ login_required(login_url='login')
def YourBusiness(request):
    context = {}
    context['catergories'] = Catergory.objects.all()
    if request.method == 'POST':
        search_text = request.POST['search_text']
        catergory_s = request.POST['catergory']

        if catergory_s == "all":
            context['businesses'] = BusinessProfile.objects.filter(Q(
                name__icontains=search_text) | Q(description__icontains=search_text), user=request.user)
        else:
            context['businesses'] = BusinessProfile.objects.filter(Q(
                name__icontains=search_text) | Q(description__icontains=search_text), catergory__name=catergory_s, user=request.user)
        return render(request, 'business/your-businesses.html', context)
    if BusinessProfile.objects.filter(user=request.user).exists():
        context['businesses'] = BusinessProfile.objects.filter(
            user=request.user)
    else:
        return redirect('business-register')
    return render(request, 'business/your-businesses.html', context)
