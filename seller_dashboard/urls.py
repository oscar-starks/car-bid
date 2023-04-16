from django.urls import path
from seller_dashboard.views import MyCars, CarDetailView, AddCar, EditImage, Advertise

urlpatterns = [
    path('', MyCars.as_view()),
    path('car/<str:car_id>/', CarDetailView.as_view()),
    path('add_car/',AddCar.as_view()),
    path('add_image/<str:car_id>/', EditImage.as_view()),
    path('advertise/<str:car_id>/', Advertise.as_view()),

]
