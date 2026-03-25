# Open: accounts/apps.py
# Make sure it has this code:

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    def ready(self):
        import accounts.models  # Ensure signal handlers are connected