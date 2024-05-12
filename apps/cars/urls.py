# from django.contrib import admin

from django.urls import path
# from cars.views import CarTestView, CarDetailView
from apps.cars.views import CarListCreateView, CarRetrieveUpdateDestroyView


urlpatterns = [
    # path('carsTest', CarTestView.as_view()),
    # path('carDetail/<int:pk>', CarDetailView.as_view()),
    # path('carDetail/<slug:pk>', CarDetailView.as_view()),
    # path('admin/', admin.site.urls),
    path('', CarListCreateView.as_view(), name='cars_'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_delete'),
]
