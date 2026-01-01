import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fashion_api.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
FIRST_NAME = os.environ.get("DJANGO_SUPERUSER_FIRST_NAME", "Admin")
LAST_NAME = os.environ.get("DJANGO_SUPERUSER_LAST_NAME", "User")

if not PASSWORD:
    raise ValueError("No superuser password set in DJANGO_SUPERUSER_PASSWORD!")

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD,
        first_name=FIRST_NAME,
        last_name=LAST_NAME
    )
    print("Superuser created!")
else:
    print("Superuser already exists.")
