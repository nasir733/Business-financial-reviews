from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import *
from companydashboard.models import *
from django.db.models import Avg
# Create your views here.


@login_required(login_url='login')
def add_review(request, business_id):
    context = {}
    business = BusinessProfile.objects.get(id=business_id)
    context['business'] = business
    if request.method == 'POST':
        review = Review.objects.create(
            business=business,
            user=request.user,
            rating=int(request.POST['rating']),
            review=request.POST['review'],
            content=request.POST['content'],
        )
        avg_rating = Review.objects.filter(
            business__id=business_id).aggregate(Avg('rating'))
        rating = round(float(avg_rating['rating__avg']), 2)
        business.avg_rating = rating
        business.save()
        print(rating)
        return render(request, 'reviews/review_added.html', {'review': review})
    return render(request, 'reviews/write-review.html', context)


@login_required(login_url='login')
def add_comment(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        comment = ReviewComment.objects.create(
            review=review,
            user=request.user,
            comment=request.POST['comment']
        )
        return redirect('business', business_id=review.business.id, page=1)
