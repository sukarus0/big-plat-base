from rest_framework import routers
from .views import ComponentStatusViewSet

router = routers.SimpleRouter()
router.register('info', ComponentStatusViewSet)

urlpatterns = router.urls
