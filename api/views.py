from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Genre, Book
from .permissions import IsAdminOrReadOnly
from .serializers import (GenreSerializer, GenreDetailSerializer,
                          BookSerializer, BookListSerializer, BookDetailSerializer)


class GenreViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'pk'

    def get_queryset(self):
        genres = Genre.objects.all().order_by('id')
        search = self.request.query_params.get('search')
        if search:
            genres = genres.filter(name__icontains=search)
        return genres

    def get_serializer_class(self):
        if self.action == 'list':
            return GenreSerializer
        return GenreDetailSerializer

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        books = Book.objects.select_related('genre').filter(genre_id=pk).order_by('id')
        return Response(BookListSerializer(books, many=True).data)


class BookViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'pk'

    def get_queryset(self):
        books = Book.objects.select_related('genre').order_by('id')
        genre_id = self.request.query_params.get('genre_id')
        if genre_id:
            books = books.filter(genre_id=genre_id)
        author = self.request.query_params.get('author')
        if author:
            books = books.filter(author__icontains=author)
        return books

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer
