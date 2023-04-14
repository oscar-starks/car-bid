from django.urls import path 
from accounts.views import CreateUser, LoginView

urlpatterns = [
    path("signup/", CreateUser.as_view(), name="signup"),
    path('login/', LoginView.as_view())

]
