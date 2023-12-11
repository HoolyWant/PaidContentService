from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('change_password/', ChangePassword.as_view(), name='change_password'),
    # path('error_password_change/', ErrorPasswordChange.as_view(), name='error_password_change')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
