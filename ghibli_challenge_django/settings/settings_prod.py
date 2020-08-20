from .settings_base import *

import os
import secrets

DEBUG = False

ALLOWED_HOSTS = [
    # My personal domain; feel free to replace with your own
    'ghibli.runhorst.dev'
]

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    # We don't have any persistent data anyway, so we can just
    # create a secret key at runtime if needed
    secrets.token_hex(32)
)
