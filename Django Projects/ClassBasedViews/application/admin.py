from django.contrib import admin
from application.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','no_of_pages','price']
admin.site.register(Book,BookAdmin)
