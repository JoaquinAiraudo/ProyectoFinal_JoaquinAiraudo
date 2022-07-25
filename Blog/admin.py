from django.contrib import admin
from .models import Post

# Register your models here.


class Post_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('titulo', 'autor')
    search_fields = ('titulo',)
    date_hierarchy = 'updated'


admin.site.register(Post, Post_admin)