from django.contrib import admin

from webapp.models import Topic, Comment

class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    list_display_links = ['id', 'user']
    list_filter = []
    search_fields = ['user', 'description']
    fields = ['user', 'title', 'description','created_at', 'reply_count']
    readonly_fields = ['created_at']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment)
