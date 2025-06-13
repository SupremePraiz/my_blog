from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    author_user = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    contents = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.contents}"
    
class Comment(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.review_user} - {self.content}'