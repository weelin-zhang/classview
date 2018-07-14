from rest_framework import serializers
from app.models import Book, Author

# blog
from blog.models import Post

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


# blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "body")
