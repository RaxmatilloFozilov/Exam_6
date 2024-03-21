from django.contrib import admin
from .models import Topic,Item


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields =('title', 'description')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields =('name', 'description')

admin.site.register(Topic, TopicAdmin)
admin.site.register(Item, ItemAdmin)

# Register your models here.
