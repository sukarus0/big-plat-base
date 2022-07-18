from rest_framework import routers
from .views import ResourceViewSet, ClusterInfoViewSet

router = routers.SimpleRouter()
router.register('resource', ResourceViewSet)
router.register('cluster_info', ClusterInfoViewSet)

urlpatterns = router.urls
