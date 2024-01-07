from django.contrib import admin

from quotes.models import Author, Quote

admin.site.register(Author)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'is_active', 'created_at')
    list_filter = ('is_active', 'groups', 'author', 'created_at')
    search_fields = ('text',)
    filter_horizontal = ('groups',)
