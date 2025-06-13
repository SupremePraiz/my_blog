from rest_framework import serializers
from account.models import Author, Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["review_user","post", "content", "date_posted"]

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    # comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='contents')
    # comments = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    

    class Meta:
        model = Author
        fields = '__all__'
        # fields = ["username", "is_active", "date_joined", "posts"]


