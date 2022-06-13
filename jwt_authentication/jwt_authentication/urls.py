from django.contrib import admin
from django.urls import path

from .token_views import CustomTokenObtainPairView

from .views import UserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenObtainSlidingView, TokenRefreshSlidingView, TokenBlacklistView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/',UserView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/token/custom/',CustomTokenObtainPairView.as_view()),

    path('api/sliding_token/',TokenObtainSlidingView.as_view()),
    path('api/sliding_token/refresh/',TokenRefreshSlidingView.as_view()),

    path('api/token/blacklist/',TokenBlacklistView.as_view())
]
