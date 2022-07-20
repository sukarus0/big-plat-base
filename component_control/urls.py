from django.urls import path
from rest_framework import routers
from .views import ComponentStatusViewSet, startComponent, stopComponent, restartComponent

router = routers.SimpleRouter()
router.register('info', ComponentStatusViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('start/', startComponent),
    path('stop/', stopComponent),
    path('restart/', restartComponent),
]
