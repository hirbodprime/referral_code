from django.apps import AppConfig


class NetworkerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'networker'
    def ready(self):
        import networker.signals