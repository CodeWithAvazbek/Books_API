from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
                                     DestroyAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     CreateAPIView
                                     )
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


# class BookListAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
class BookListAPIView(APIView):
    def get(self, request):
        try:
            books = Book.objects.all()
            serializers = BookSerializers(books, many=True)
            success = {
                "Status": True,
                "Data": serializers.data
            }
            return Response(success)
        except:
            problem = {
                "Status": False,
                "Message": "Book Not found"
            }
            return Response(problem)


# class BookDeleteAPIView(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     lookup_field = "id"
class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.filter(id=pk).first()
            book.delete()
            success = {
                "Status": True,
                "Message": "Successfully (Deleted)"
            }
            return Response(success)
        except:
            problem = {
                "Status": False,
                "Message": "Book Not found"
            }
        return Response(problem)


# class BookDetailAPIView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     lookup_field = "id"
class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(id=pk).first()
        if book:
            serializer = BookSerializers(book)
            success = {
                "Status": True,
                "Data": serializer.data
            }
            return Response(success, 200)
        problem = {
            "Status": False,
            "Data": "Book not found"
        }
        return Response(problem, 404)


# class BookUpdateAPIView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     lookup_field = "id"
class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        data = request.data
        serializer_data = BookSerializers(instance=book, data=data, partial=True)
        if serializer_data.is_valid(raise_exception=True):
            serializer_data.save()
            update_book = serializer_data.data
            success = {
                "Status": True,
                "Data": update_book
            }
            return Response(success, 201)
        problem = {
            "Status": False,
            "Data": "Mistake"
        }
        return Response(problem, 404)


# class BookCreateAPIView(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


class BookCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer_data = BookSerializers(data=data)
        if serializer_data.is_valid(raise_exception=True):
            serializer_data.save()
            success = {
                "Status": True,
                "Data": data
            }
            return Response(success, 201)
        problem = {
            "Status": False,
            "Data": "Mistake"
        }
        return Response(problem, 404)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
