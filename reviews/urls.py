from django.urls import path
from . import views
urlpatterns = [
    path('add/<int:business_id>', views.add_review, name='add_review'),
    path('delete-review/<int:review_id>/',
         views.deletereview_detail, name='deletereview_detail'),
    path('addcomment/<int:review_id>', views.add_comment, name='add_comment'),
]
