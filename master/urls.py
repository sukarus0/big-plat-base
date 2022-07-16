from rest_framework import routers
from .views import BigDataComponentViewSet

router = routers.SimpleRouter()
router.register('big-data-component', BigDataComponentViewSet)

urlpatterns = router.urls
