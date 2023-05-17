from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LoginView, UserView, ProfileView, PasswordResetAPIView, ChangePasswordAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserView.as_view(), name='user'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password-reset/', PasswordResetAPIView.as_view(), name='password_reset'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
]
