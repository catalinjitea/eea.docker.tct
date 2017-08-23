from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):

    help = 'Loads to database the initial objects'

    def handle(self, *args, **options):
        for fixture in ('scales', 'aichi_links', 'aichi_indicators',
                        'aichi_targets', 'aichi_goals', 'pages', 'cms_targets',
                        'cms_goals', 'ramsar_targets', 'ramsar_goals'):
            call_command('loaddata', fixture)

        if settings.EU_STRATEGY:
            for fixture in ('eu_actions', 'eu_indicators', 'eu_targets',
                            'eu_aichi_mapping', 'eu_aichi_indicators_mapping'):
                call_command('loaddata', fixture)
