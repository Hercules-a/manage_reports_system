from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ProblemViewSet, OrderViewSet, PartStageViewSet, PartViewSet, CarViewSet

router = routers.DefaultRouter()
router.register(r'problemy', ProblemViewSet, basename='problem')
router.register(r'zlecenia', OrderViewSet, basename='order')
router.register(r'stany_generacyjne', PartStageViewSet, basename='part_stage')
router.register(r'czesci', PartViewSet, basename='part')
router.register(r'uzytkownicy', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]
