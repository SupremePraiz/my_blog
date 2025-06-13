from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import AdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .throttle import CommentListThrottle, CommentDetailThrottle

from account.models import Author, Post, Comment
from .serializers import AuthorSerializer, PostSerializer, CommentSerializer
from .pagination import AuthorPagination



class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    pagination_class = AuthorPagination
    # permission_classes = [IsAuthenticated]

    '''this is for filtering'''
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']

    '''this is for odering'''
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['username']

    
    
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AdminOrReadOnly]
   


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title','author__username']

    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return Post.objects.filter(author=pk)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'title']


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [CommentListThrottle]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(post=pk)
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    '''this is for searching'''
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'title']
    # permission_classes = [IsAuthenticated]