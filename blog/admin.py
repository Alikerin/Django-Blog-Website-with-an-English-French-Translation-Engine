# @Author: Ibrahim Salihu Yusuf <yusuf>
# @Date:   2020-03-20T14:23:12+02:00
# @Email:  sibrahim1396@gmail.com
# @Last modified by:   yusuf
# @Last modified time: 2020-03-25T17:44:32+02:00


from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment, Project

class PostAdmin(SummernoteModelAdmin):
    list_display = ["title", "slug", "status", "created_on"]
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug":("title",)}
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class ProjectAdmin(SummernoteModelAdmin):
    list_display = ["title", "status", "created_on"]
    list_filter = ("status",)
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug":("title",)}
    summernote_fields = ('description',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Project, ProjectAdmin)
