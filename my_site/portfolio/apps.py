from django.apps import AppConfig
# файл содержащий класс, отвечающщйи за поведение приложения

class PortfolioConfig(AppConfig): # Класс, отвечающий за поведение приложения
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
