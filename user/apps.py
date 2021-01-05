from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = "user"

    def ready(self):
        from . import signals
