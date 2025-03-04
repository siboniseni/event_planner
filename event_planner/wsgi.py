"""WSGI config for the event_planner project.

This module exposes the WSGI callable as a module-level variable named `application`,
which Django’s commands and some deployment setups use to communicate with your
web application.

For details, see:
    https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_planner.settings')

application = get_wsgi_application()

