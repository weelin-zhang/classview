from rest_framework import serializers
from ..models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # 外键存在可以用来迁移,归属作者
        fields = ("name", "price", "id", "author")


class AuthorSerializer(serializers.ModelSerializer):

    # books嵌套序列化
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ("id", "name", "books")

