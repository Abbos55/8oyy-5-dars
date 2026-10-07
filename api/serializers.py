from rest_framework import serializers

from .models import Genre, Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['description']


class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'min_length': 2},
        }


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['pages', 'published_year']
        depth = 1


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'price': {'min_value': 0},
            'pages': {'min_value': 1},
            'published_year': {'min_value': 1000, 'max_value': 2100},
        }
