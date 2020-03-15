from django.contrib import admin
from application.models import Sample
# Register your models here.
class SampleAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Sample,SampleAdmin)
