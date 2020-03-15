from django.contrib import admin
from application.models import Reporter,Article,Publication,Article2,Place,Restaurant,Waiter
# Register your models here.

class ReporterAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email']
class ArticleAdmin(admin.ModelAdmin):
    list_display=['headline','pub_date','reporter']
class PublicationAdmin(admin.ModelAdmin):
    list_display=['title']
class Article2Admin(admin.ModelAdmin):
    list_display=['headline','get_publications']
class PlaceAdmin(admin.ModelAdmin):
    list_display=['name','address']
class RestaurantAdmin(admin.ModelAdmin):
    list_display=['place','serves_hot_dogs','serves_pizza']
class WaiterAdmin(admin.ModelAdmin):
    list_display=['restaurant','name']
admin.site.register(Reporter,ReporterAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Article2,Article2Admin)
admin.site.register(Place,PlaceAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Waiter,WaiterAdmin)
