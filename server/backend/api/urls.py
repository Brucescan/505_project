from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    GetCurrentUserView,
    SearchUsersView,
    DeleteUserView
)

urlpatterns = [
    path('api/user/register', UserRegisterView.as_view(), name='user-register'),
    path('api/user/login', UserLoginView.as_view(), name='user-login'),
    path('api/user/logout', UserLogoutView.as_view(), name='user-logout'),
    path('api/user/current', GetCurrentUserView.as_view(), name='get-current-user'),
    path('api/user/search', SearchUsersView.as_view(), name='search-users'),
    path('api/user/delete/<int:id>', DeleteUserView.as_view(), name='delete-user'),
]
