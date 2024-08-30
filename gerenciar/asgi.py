"""
ASGI config for gerenciar project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
#Nessa parte e aonde fica a configuração para para comunicar com o seu projeto Django e processar as requisições HTTP.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciar.settings')

application = get_asgi_application()
