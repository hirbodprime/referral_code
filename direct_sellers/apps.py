from django.apps import AppConfig


class DirectSellerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'direct_sellers'
    def ready(self):
        import direct_sellers.signals