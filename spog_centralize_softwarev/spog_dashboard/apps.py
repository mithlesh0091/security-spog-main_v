from django.apps import AppConfig

class SpogDashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spog_dashboard'

    def ready(self):
        import spog_dashboard.signals  # 👈 This line imports your signals
