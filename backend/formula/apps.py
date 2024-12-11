from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'formula'  # Deve corresponder ao nome do diretório do aplicativo
