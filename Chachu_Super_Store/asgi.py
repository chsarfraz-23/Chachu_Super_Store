import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Chachu_Super_Store.settings")

application = get_asgi_application()
