from django.apps import AppConfig


class BlogConfig(AppConfig): # класс, необходимый для управлением приложения, через него осуществляется связь основного проекта и приложения
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name='Блог' # Переменная, пределяющая под каким именем будет отображаться приложение в том числе в админ панели
