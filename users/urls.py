from django.urls import path
from users.views import RegisterView, LoginView

app_name = 'users'

urlpatterns = [
    path('api/accounts/register/', RegisterView.as_view(), name='register'),
    path('api/accounts/login/', LoginView.as_view(), name='login'),
]