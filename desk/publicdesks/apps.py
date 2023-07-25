from django.apps import AppConfig


class PublicdesksConfig(AppConfig):
    name = 'publicdesks'

    def ready(self):
        import publicdesks.signals