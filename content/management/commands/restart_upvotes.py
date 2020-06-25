from django.core.management.base import BaseCommand, CommandError
from content.models import Upvote


class Command(BaseCommand):
    help = 'Restart upvotes. Use once a day'

    def handle(self, *args, **options):
        [upvote.users.clear() for upvote in Upvote.objects.all()]
