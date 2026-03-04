import os
import sys

# Add the project path to the sys.path
sys.path.append(os.path.dirname(__file__))

# Set the settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()