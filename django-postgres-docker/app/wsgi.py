# filepath: c:\Users\gabri\Downloads\DjangoContenedor\django-postgres-docker\app\wsgi.py
"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 👇 Asegúrate de que 'app.settings' coincida con tu archivo de configuración
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()