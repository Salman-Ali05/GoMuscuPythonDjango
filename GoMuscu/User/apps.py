from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GoMuscu.User'

def ready(self):
        import GoMuscu.User.signals  
