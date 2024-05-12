from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    # print(query.items())
    for k, v in query.items():
        match k:
            case 'price__gt':
                qs = qs.filter(price__gt=v)
            case 'brand__contains':
                qs = qs.filter(brand__icontains=v)
            case _:
                raise ValidationError(f"'{k}' is not valid")
    return qs
