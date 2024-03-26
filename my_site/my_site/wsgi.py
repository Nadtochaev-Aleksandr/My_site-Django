"""
WSGI config for my_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
# Данный файл необходим для развертывания сайта на реальном веб сервере. Содержит свойства кофигурации WSGIc
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')

application = get_wsgi_application()
