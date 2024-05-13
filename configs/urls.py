# from django.contrib import admin

from django.urls import path
# from cars.views import CarTestView, CarDetailView
from apps.cars.views import CarListCreateView


urlpatterns = [
    # path('carsTest', CarTestView.as_view()),
    # path('carDetail/<int:pk>', CarDetailView.as_view()),
    # path('carDetail/<slug:pk>', CarDetailView.as_view()),
    # path('admin/', admin.site.urls),
    path('cars', CarListCreateView.as_view())
]
