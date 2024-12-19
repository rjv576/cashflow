from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TransactionViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'transactions',TransactionViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'category',CategoryViewSet)

urlpatterns = [
    path("api/v1/",include(router.urls)),
]
