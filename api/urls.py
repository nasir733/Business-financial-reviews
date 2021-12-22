from rest_framework import routers
from .views import *
from django.urls import path
router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'business', BusinessViewSet)

urlpatterns = [
    path('', BusinessApiView.as_view()),
]
urlpatterns += router.urls
