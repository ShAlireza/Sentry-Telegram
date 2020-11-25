import hmac
import json
from _sha256 import sha256

from django.conf import settings

from rest_framework.permissions import BasePermission


class IsSentry(BasePermission):

    def has_permission(self, request, view):
        body = json.dumps(request.body)
        expected = hmac.new(
            key=settings.SENTRY_CLIENT_KEY.encode('utf-8'),
            msg=body,
            digestmod=sha256
        ).hexdigest()

        if expected != request.headers['Sentry-Hook-Signature']:
            return False
        return True
