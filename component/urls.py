from rest_framework import routers
from .views import ResourceViewSet

router = routers.SimpleRouter()
router.register('resource', ResourceViewSet)

urlpatterns = router.urls
