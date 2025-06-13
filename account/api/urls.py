from django.urls import path
from .views import AuthorListCreateView,AuthorDetailView, PostListCreateView, PostDetailView, CommentListView, CommentDetailView

urlpatterns = [
    path("author/", AuthorListCreateView.as_view(), name="author-list-create"),
    path("author/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),

    path("author/post/", PostListCreateView.as_view(), name="post-list-create"),
    path("author/post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    path("post/<int:pk>/comment/", CommentListView.as_view(), name="comment-list-create"),
    path("post/comment/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    
]
