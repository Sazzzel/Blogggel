from django.contrib import admin
from .models import Post, Comment, Testimonial
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'article']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('article',)

# Register your models here.


admin.site.register(Comment)
admin.site.register(Testimonial)
