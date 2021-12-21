from rest_framework import routers
from .views import *
router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'business', BusinessViewSet)
urlpatterns = router.urls
