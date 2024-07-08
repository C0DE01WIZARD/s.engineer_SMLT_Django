from django.apps import AppConfig


class ServiceConfig(AppConfig):
    verbose_name = 'Техническое обслуживание'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service_app'
