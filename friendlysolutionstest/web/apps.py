from django.apps import AppConfig


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'friendlysolutionstest.web'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        import friendlysolutionstest.web.signals
