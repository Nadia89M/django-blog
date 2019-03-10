from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at')
    list_display_links = ('id','title')
    list_filter = ('title',)
    search_fields = ('title', )
    list_per_page = 25

admin.site.register(Post, PostAdmin)