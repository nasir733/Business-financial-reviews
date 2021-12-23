from django.shortcuts import redirect, render
from catergory.models import Catergory
from companydashboard.models import BusinessProfile
from reviews.models import Review
# Create your views here.
from django.db.models import Avg
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django import template

register = template.Library()


@register.filter
def page_window(page, last, size=7):
    if page < size // 2 + 1:
        # remember the range function won't
        return range(1, min(size+1, last + 1))
        # include the upper bound in the output
    else:
        return range(page - size // 2, min(last + 1, page + 1 + size // 2))


def HomePage(request):
    context = {}
    data = Catergory.objects.all().order_by('?')[:6]
    request.session['catergories'] = list(data.values())
    context['reviews'] = Review.objects.all().order_by('?')[:4]
    context['catergories'] = Catergory.objects.all().order_by('?')[:6]
    return render(request, 'main/index.html', context)


def BusinessList(request, catergory="all"):
    context = {}
    page = request.GET.get('page', 1)
    if request.method == "POST":
        search_text = request.POST['search_text']
        catergory_s = request.POST['catergory']

        if catergory_s == "all":
            context['businesses'] = BusinessProfile.objects.filter(Q(
                name__icontains=search_text) | Q(description__icontains=search_text))
        else:
            context['businesses'] = BusinessProfile.objects.filter(Q(
                name__icontains=search_text) | Q(description__icontains=search_text), catergory__name=catergory_s)
        context['catergory'] = catergory_s
        context['results'] = len(context['businesses'])
        context['catergories'] = Catergory.objects.all()
        return render(request, 'main/business_list.html', context)
    if catergory == "all":
        context['businesses'] = BusinessProfile.objects.all()

    else:
        context['businesses'] = BusinessProfile.objects.filter(
            catergory__name=catergory)
    context['catergory'] = catergory
    context['results'] = len(context['businesses'])
    context['catergories'] = Catergory.objects.all()
    paginator = Paginator(context['businesses'], 10)
    context['paginatedBusinesses'] = paginator.page(page)

    return render(request, 'main/business_list.html', context)


def BusinessSingle(request, business_id, page=1):

    context = {}
    reviews = Review.objects.filter(business__id=business_id)
    paginator = Paginator(reviews, 10)
    context['business'] = BusinessProfile.objects.get(id=business_id)
    if context['business'].user.id == request.user.id:
        return redirect('business:dashboard', name=context['business'].name, page=page)
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
        context['five_star'] = len(five_star)/len(context['reviews'])*100
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
    return render(request, 'main/business_single.html', context)


def allcatergories(requesst):
    context = {}
    context['catergories'] = Catergory.objects.all()
    return render(requesst, 'main/all-categories.html', context)
