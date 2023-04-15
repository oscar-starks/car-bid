from django.urls import path
from seller_dashboard.views import MyCars

urlpatterns = [
    path('', MyCars.as_view()),

]
