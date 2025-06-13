from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import registration_view

# urlpatterns = [
#     path("login/", ObtainAuthToken.as_view(), name="login"),
#     path("register/", registration_view, name="register"),
# ]


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("register/", registration_view, name="register"),
]

