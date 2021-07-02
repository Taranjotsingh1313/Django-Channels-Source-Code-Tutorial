"""
ASGI config for channels_tut project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import URLRouter,ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from .routing import ws_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_tut.settings')

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
        URLRouter(
            ws_application
        )
        )
    )
})
