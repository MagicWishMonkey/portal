"""
WSGI config for metrics project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")

application = get_wsgi_application()