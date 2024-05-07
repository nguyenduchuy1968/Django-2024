# from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from cars.models import CarModel
from .serializers import CarSerializer
from rest_framework import status

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


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        # res = [{'id':car.pk, 'brand': car.brand, 'price': car.price, 'year': car.year} for car in cars]
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        # CarModel.objects.create(**serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED)

class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
            # return Response('Car not Found', status.HTTP_404_NOT_FOUND)
        # car_res = {'id': car.pk, 'brand': car.brand, 'price': car.price, 'year': car.year}
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
            # return Response('Car not Found', status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # for key, value in data.items():
        #     setattr(car, key, value)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
            # return Response('Car not Found', status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # for key, value in data.items():
        #     setattr(car, key, value)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            CarModel.objects.get(pk=pk).delete()
        except CarModel.DoesNotExist:
            raise Http404()
            # return Response('Car not Found', status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
