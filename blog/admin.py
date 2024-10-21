from django.contrib import admin
from .models import Blog, Category, Comment
from django.utils.safestring import mark_safe

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug",)
    list_editable = ("is_active","is_home",)
    search_fields = ("title","description",)
    readonly_fields = ("slug",)
    list_filter = ("is_active", "is_home", "categories")

def selected_categories(self, obj):
    html = "<ul>"

    for category in obj.categories.all():
        html += "<li>" + category.name + "</li>"
    
    html = "</ul>"
    return mark_safe(html)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
