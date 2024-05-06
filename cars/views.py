# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from cars.models import CarModel

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
        res = [{'brand': car.brand, 'price': car.price, 'year': car.year} for car in cars]
        return Response(res)


    def post(self, *args, **kwargs):
        data = self.request.data
        CarModel.objects.create(**data)
        return Response('Created')