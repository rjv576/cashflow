from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TransactionViewSet, CategoryViewSet,CustomUserViewSet, RegisterUserView

router = DefaultRouter()
router.register(r'transactions',TransactionViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'users',CustomUserViewSet)
urlpatterns = [
    path("api/v1/",include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),  # Proporciona el token de autenticación
]
