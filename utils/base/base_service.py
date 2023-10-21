from django.core.exceptions import ValidationError
from django.db import models
from django.http import JsonResponse
from rest_framework import serializers, status


class BaseService:
    model = None  # This must be set by inheriting classes

    @classmethod
    def create(cls, **kwargs):
        try:
            obj = cls.model(**kwargs)
            obj.full_clean()
            obj.save()
        except ValidationError as e:
            raise ValidationError(str(e))
        return obj

    @classmethod
    def get_all(cls):
        return cls.model.objects.all()

    @classmethod
    def get_by_id(cls, object_id):
        try:
            objects = cls.model.objects.get(pk=object_id)
        except cls.model.DoesNotExist:
            raise serializers.ValidationError(f"{cls.model.__name__} does not exist.")
        return objects

    @classmethod
    def update(cls, object_id, **kwargs):
        obj = cls.get_by_id(object_id)
        for attr, value in kwargs.items():
            setattr(obj, attr, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, object_id):
        obj = cls.get_by_id(object_id)
        obj.delete()
        return JsonResponse({"message": f"{cls.model.__name__} deleted successfully."}, status=status.HTTP_200_OK)

    @classmethod
    def filter(cls, parameters: dict, prefetch_: list, select_: list):
        return cls.model.objects.filter(**parameters).prefetch_related(*prefetch_).select_related(*select_)
