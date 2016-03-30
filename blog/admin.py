from django.contrib import admin
from .models import Post, Comment

# The admin iterface for Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'body')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    
# The admin iterface for Comment model
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updateed')
	search_fields = ('name', 'email', 'body')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)