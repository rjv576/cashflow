from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'transactions',TransactionViewSet)
router.register(r'projects', ProjectViewSet)


urlpatterns = [
    path("api/v1/",include(router.urls)),
]
