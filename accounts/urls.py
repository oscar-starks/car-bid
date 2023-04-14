from django.urls import path 
from accounts.views import CreateUser, LoginView, UserProfile, Logout, ForgotPassword, NewPasswordView, CheckTokenView, ChangePasswordView

urlpatterns = [
    path("signup/", CreateUser.as_view(), name="signup"),
    path('login/', LoginView.as_view()),
    path('profile/', UserProfile.as_view()),
    path('logout/', Logout.as_view()),
    path('forgot_password/', ForgotPassword.as_view()),
    path('check_token/', CheckTokenView.as_view()),
    path('new_password/', NewPasswordView.as_view()),
    path('change_password/', ChangePasswordView.as_view())
]
