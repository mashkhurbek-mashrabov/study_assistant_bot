from celery import shared_task

from quotes.models import Quote
from university.models import Group
from bot.loader import bot


@shared_task
def sending_daily_quote_task():
    groups = Group.objects.filter(is_active=True, telegram_id__isnull=False).prefetch_related('quotes')
    for group in groups:
        try:
            quote = group.quotes.filter(is_active=True, was_send=False).order_by('created_at').first()
            if quote:
                bot.send_message(chat_id=group.telegram_id, text=quote.text, parse_mode='HTML')
                quote.was_send = True
                quote.save()
        except IndexError:
            continue

@shared_task
def send_selected_quote_task(quote_ids: list):
    quotes = Quote.objects.filter(id__in=quote_ids).prefetch_related('groups')
    for quote in quotes:
        for goup in quote.groups.all():
            bot.send_message(chat_id=goup.telegram_id, text=quote.text, parse_mode='HTML')
            quote.was_send = True
            quote.save()