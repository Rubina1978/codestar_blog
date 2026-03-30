from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)  # allowes me to create, update and delete blog posts from admin panel.