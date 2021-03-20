from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
from .views import RegistrationAPIView, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'registration', RegistrationAPIView, basename='registration')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
              ] + router.urls


# urlpatterns = [
#     re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
#     re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
# ]


