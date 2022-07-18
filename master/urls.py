from rest_framework import routers
from .views import BigDataComponentViewSet

router = routers.SimpleRouter()
router.register('master', BigDataComponentViewSet)

urlpatterns = router.urls
