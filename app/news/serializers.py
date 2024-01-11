from rest_framework import serializers
from .models import News
from rest_framework.exceptions import ValidationError


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'summary',
            'details',
            'news_reference',
            'news_title_persian',
            'news_summary_persian',
            'news_reference_persian',
            'date',
            'faculty',
        ]
    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data