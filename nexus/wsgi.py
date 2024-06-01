"""
WSGI config for nexus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexus.settings')

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'staticfiles')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
app = application
