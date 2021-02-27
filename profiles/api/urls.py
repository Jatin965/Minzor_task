from django.urls import path, include
from .views import CustomerModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('customer', CustomerModelViewSet)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name = 'obtain-pair'),
    path('refresh/', TokenRefreshView.as_view(), name = 'token-refresh')
]