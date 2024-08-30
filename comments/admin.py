# from django.contrib import admin
# from .models import Comment

# # Register your models here.

# admin.site.register(Comment)



# from django.db import models
# from django.contrib.auth.models import User 
# from posts.models import Post


# # Create your models here.
# class Comment(models.Model):
#     """
#     Comment model, related to User and Post
#     """
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     content = models.TextField()

#     class Meta:
#         ordering= ['-created_at']

#     def __str__(self):
#         return f'{self.post} {self.content}'
