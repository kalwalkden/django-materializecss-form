from django.conf import settings

MATERIALIZECSS_COLUMN_COUNT = getattr(settings, 'MATERIALIZECSS_COLUMN_COUNT', 12)
