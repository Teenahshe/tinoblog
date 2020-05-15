from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Comment
from django.contrib.auth.models import User, Group

# Register your models here.
admin.site.site_header = "TinoClare's Blog"
admin.site.site_title = "TinoClare's Blog"
admin.site.index_title = "Welcome to TinoClare's Blog"

admin.site.unregister(Group)

class BlogAdmin(SummernoteModelAdmin):
	summernote_fields = ('blog_content')
	list_display = ('author', 'title', 'category', 'date_published')
	list_filter = ('author', 'title', 'category', 'date_published')
	search_fields = ['author', 'title', 'category', 'date_published', 'blog_content', 'sub_title']
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Blog, BlogAdmin)

class CommentAdmin(SummernoteModelAdmin):
	list_display = ('blog','user','approved_comment')
	list_filter = ('blog','user','approved_comment')
	search_fields = ['blog','user','approved_comment']
	actions = ['approve_comments']

	def approve_comments(self, request, queryset):
		queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)