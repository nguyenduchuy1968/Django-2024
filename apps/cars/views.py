# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.models import CarModel
from .filters import car_filter
from .serializers import CarSerializer


# class CarTestView(APIView):
#     def get(self, *args, **kwargs):
#         return Response("Hello from GET")
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         params_dict = self.request.query_params.dict()
#         print(params_dict)
#         print(data)
#         return Response("Hello from POST")
#
#     def put(self, *args, **kwargs):
#         return Response("Hello from PUT")
#
#     def patch(self, *args, **kwargs):
#         return Response("Hello from PATCH")
#
# class CarDetailView(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         return Response("Hello from GET")
#
#     def delete(self, *args, **kwargs):
#         return Response("Hello from DELETE")


# ======================================
#
# class CarListCreateView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#     def get(self, *args, **kwargs):
#         # cars = CarModel.objects.all()
#         # cars = CarModel.objects.filter(brand='Volvo', year=2019)
#         # cars = CarModel.objects.filter(brand__in=['Volvo', 'Mercedes', 'Volkswagen'], year=2000)
#         # cars = CarModel.objects.filter(brand__contains='o')
#         # cars = CarModel.objects.filter(year__range=(2000, 2022)).order_by('-year')
#         # cars = CarModel.objects.order_by('-year', '-id')
#
#         # queryset
#         # qs = CarModel.objects.all().exclude(brand='Kia')
#         # qs = CarModel.objects.all()
#         # qs = qs[1:2].only('id', 'brand')
#         # print(qs.query)
#
#         # qs = car_filter(self.request.query_params.dict())
#         # qs = car_filter(self.request.query_params.dict())
#
#         qs = self.get_queryset()
#         serializer = self.get_serializer(qs, many=True)
#         print('get', serializer)
#         print('get', serializer.data)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#         # qs = CarModel.objects.filter(Q(brand='Kia') | Q(year=2022))
#         # serializer = CarSerializer(qs, many=True)
#         # return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = self.get_serializer(data=data)
#
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#         print('post', serializer)
#         # CarModel.objects.create(**serializer.data)
#         return Response(serializer.data, status.HTTP_201_CREATED)
#

# =========================================
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         print('car', car)
#         # pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#             # return Response('Car not Found', status.HTTP_404_NOT_FOUND)
#
#         # car_res = {'id': car.pk, 'brand': car.brand, 'price': car.price, 'year': car.year}
#
#         # car = get_object_or_404(CarModel, pk=pk)
#         serializer = CarSerializer(car)
#         # serializer = self.get_serializer(car)
#         print('car-2', serializer)
#         print('car-3', serializer.data)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#             # return Response('Car not Found', status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = self.get_serializer(car, data=data)
#         print('put', serializer)
#
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         # for key, value in data.items():
#         #     setattr(car, key, value)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#             # return Response('Car not Found', status.HTTP_404_NOT_FOUND)
#
#         car = self.get_object()
#         serializer = self.get_serializer(car, data, partial=True)
#         print('PATCH', serializer)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         # for key, value in data.items():
#         #     setattr(car, key, value)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print('PATCH2', serializer)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     CarModel.objects.get(pk=pk).delete()
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#             # return Response('Car not Found', status.HTTP_404_NOT_FOUND)
#
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#==========================================

# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

#=========================================

class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer



