from django.apps import AppConfig


class VehicleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.vehicle"

    def ready(self):
        # for registry
        import backend.vehicle.dashboards  # type: ignore # noqa
