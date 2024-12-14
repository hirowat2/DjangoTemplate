from django.apps import AppConfig


class KitchenSinkConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.kitchensink"

    def ready(self):
        # for registry
        import backend.kitchensink.dashboards  # type: ignore # noqa
