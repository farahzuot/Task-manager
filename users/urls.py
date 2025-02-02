from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import RegisterView, LoginAPIView, CustomLogin

app_name = 'users'

urlpatterns = [
    path('api/accounts/register/', RegisterView.as_view(), name='register_api'),
    path('api/accounts/login/', LoginAPIView.as_view(), name='login_api'),
    path('accounts/logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('accounts/login/', CustomLogin.as_view(next_page='/tasks'), name='login'),
]