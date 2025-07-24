from django.urls import path
from .views import *


app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("login-with-email/", login_with_email_view, name="login_with_email"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("change-password/", change_password, name="change-pass"),
    path("reset-password/", password_reset, name="password_reset"),
    path("reset-password-confirm/<str:uid>/<str:token>",password_reset_confirm, name="confirm" )

]

