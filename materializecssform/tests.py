import unittest

import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "name": ":memory:"}},
    MIDDLEWARE_CLASSES=[],
    INSTALLED_APPS=[],
)
django.setup()


class TestTags(unittest.TestCase):
    def test_materializecss_tag(self):
        from materializecssform.templatetags import materializecss  # noqa


if __name__ == "__main__":
    unittest.main()
