from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price']

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        price = data.get('price', None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "Error": "Kitob sarlavhasi harflardan tashkil topgan bulishi kerak"
                }
            )
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "Error": "Sarlavha va Author bir xil bulmasligi kerak"
                }
            )
        if price < 0 or price > 999999:
            raise ValidationError(
                {
                    "Error": "Narx juda qmmat yoki juda arzon"
                }
            )
        return data
