from django.contrib import admin

# Register your models here.

from .models import Author,Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    


admin.site.register(Author)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)