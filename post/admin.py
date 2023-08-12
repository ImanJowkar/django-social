from django.contrib import admin
from post import models


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('body', 'slug', 'updated')
    search_fields = ('body',)
    list_filter = ('updated',)
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('publisher',)


admin.site.register(models.Post, PostAdmin)
