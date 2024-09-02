"""
WSGI config for lmsapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Add the project's base directory to the Python path to ensure the application finds all necessary modules
sys.path.append('/path/to/your/project')  # Update this with the actual path to your project if necessary

# Set the default settings module for the 'django' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lmsapp.settings')

# Get the WSGI application for the project
application = get_wsgi_application()
