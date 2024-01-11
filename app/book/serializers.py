from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'location']


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'faculty_name', 'person']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_persian']


class SectionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Section
        fields = ['id', 'category', 'section', 'section_persian']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    publisher = PublisherSerializer()
    section = SectionSerializer()
    faculty = FacultySerializer()
    language = LanguageSerializer()

    class Meta:
        model = Book
        fields = ['id', 'authors', 'publisher', 'section', 'faculty', 'language', 'signatory', 'title', 'description',
                  'isbn', 'pages', 'edition', 'publication_year']


class EBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = EBook
        fields = ['id', 'book', 'extension']


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Copy
        fields = ['id', 'book', 'status']
        

class LibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libraries
        fields=['faculty','content','content_persian','privacy','privacy_persian','services',
                'services_persian','email']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data
        

