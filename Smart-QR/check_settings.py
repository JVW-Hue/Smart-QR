import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qr_app.settings')

import django
django.setup()

from django.conf import settings
print(f"Current settings module: {settings.SETTINGS_MODULE}")
print(f"Root URLconf: {settings.ROOT_URLCONF}")
print("QR Cody app is configured correctly!")