"""
Default application configuration.
In use as of Django 1.7.
"""
from django.apps import AppConfig
from django.conf import settings
from django.db.models import signals
try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module  # Django 1.6 / py2.6
from .signals import create_notice_types


class PostmanConfig(AppConfig):
    name = 'postman'

    def ready(self):
        from .models import setup
        setup()

        name = getattr(settings, 'POSTMAN_NOTIFIER_APP', 'notification')
        if name and name in settings.INSTALLED_APPS:
            # Technically this should have a sender=notification app, but I can't get it to work!
            signals.post_migrate.connect(create_notice_types)
