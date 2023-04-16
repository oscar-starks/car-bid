from django.urls import path
from seller_dashboard.views import MyCars, CarDetailView, AddCar, AddImage

urlpatterns = [
    path('', MyCars.as_view()),
    path('car/<str:car_id>/', CarDetailView.as_view()),
    path('add_car/',AddCar.as_view()),
    path('add_image/<str:car_id>/', AddImage.as_view())

]
