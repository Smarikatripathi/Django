from django.contrib import admin

# Register your models here.
from .models import Post,Comment


admin.site.register(Post)
admin.site.register(Comment) # Register the Comment model with the admin site
