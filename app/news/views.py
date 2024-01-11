from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def validate_unknown_fields(self, data):
        """
        Validate that only fields defined in the serializer are present.
        """
        unknown = set(data) - set(self.serializer_class.Meta.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data

    def create(self, request, *args, **kwargs):
        data = request.data
        validated_data = self.validate_unknown_fields(data)
        serializer = self.get_serializer(data=validated_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data
        validated_data = self.validate_unknown_fields(data)
        serializer = self.get_serializer(instance, data=validated_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
