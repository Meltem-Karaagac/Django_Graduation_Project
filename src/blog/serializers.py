
from rest_framework import serializers
from .models import Post, Comment, Category


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'post_id')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.CharField(source="author.user_name", read_only=True)
    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'excerpt',
            'content',
            'image',
            'category',
            'status',
            'comment_count',
            'view_count',
            'like_count',
            'published',
            'comments',
        )
