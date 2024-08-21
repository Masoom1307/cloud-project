from django.core.management.base import BaseCommand
from django.urls import get_resolver

class Command(BaseCommand):
    help = 'Displays all available URLs'

    def handle(self, *args, **kwargs):
        resolver = get_resolver()
        for pattern in resolver.url_patterns:
            print(pattern)
