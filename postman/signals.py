import django.dispatch
from django.utils.translation import ugettext_noop as _
from django.conf import settings
try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module  # Django 1.6 / py2.6


def create_notice_types(*args, **kwargs):
    name = getattr(settings, 'POSTMAN_NOTIFIER_APP', 'notification')
    if name and name in settings.INSTALLED_APPS:
        notification = import_module(name + '.models')
        create = notification.NoticeType.create
        create("postman_rejection", _("Message Rejected"), _("Your message has been rejected"))
        create("postman_message", _("Message Received"), _("You have received a message"))
        create("postman_reply", _("Reply Received"), _("You have received a reply"))


msg_accepted_notification_sending = django.dispatch.Signal(providing_args=["message"])
msg_read = django.dispatch.Signal(providing_args=["message"])
