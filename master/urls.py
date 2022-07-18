from rest_framework import routers
from .views import BigDataComponentViewSet

router = routers.SimpleRouter()
router.register('component_list', BigDataComponentViewSet)

urlpatterns = router.urls
