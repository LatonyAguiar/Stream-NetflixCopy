"""
WSGI config for tonyflix project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# Esse arquivo que vai comfigurar a forma que o servidor vai se comportar quando 
# tiver varias pessoas fazendo duiversadas requisioções ao mesmo tempo no site

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tonyflix.settings')

application = get_wsgi_application()
