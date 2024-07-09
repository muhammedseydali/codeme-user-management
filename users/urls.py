from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [
#     path('', UserListCreateView.as_view(), name='user-list-create'),
#     path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
#     path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
#     path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),
#     path('permissions/', PermissionListCreateView.as_view(), name='permission-list-create'),
#     path('permissions/<int:pk>/', PermissionDetailView.as_view(), name='permission-detail'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

from django.urls import path
from .views import (
    UserListCreateAPIView,
    UserDetailAPIView,
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserChangePasswordView,
    SendPasswordResetEmailView,
    UserPasswordResetView,
)

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]




