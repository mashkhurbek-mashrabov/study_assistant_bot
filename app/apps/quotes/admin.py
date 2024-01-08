from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from quotes.tasks import send_selected_quote_task

from quotes.models import Author, Quote

admin.site.register(Author)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'is_active', 'created_at')
    list_filter = ('is_active', 'groups', 'author', 'created_at')
    search_fields = ('text',)
    filter_horizontal = ('groups',)
    actions = ('send_quote_action',)

    def send_quote_action(self, request, queryset):
        send_selected_quote_task.delay(queryset.values_list('id', flat=True))

    send_quote_action.short_description = _('Send selected quotes')
