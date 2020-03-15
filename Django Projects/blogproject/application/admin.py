from django.contrib import admin
from application.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','update','status']
    list_filter=('title','author',)
    prepopulated_fields={'slug':('title','author')}
    raw_id_fields=('author',)
    search_fields=('title','body')
    ordering=['title','author']
    date_hierarchy='publish'
admin.site.register(Post,PostAdmin)
