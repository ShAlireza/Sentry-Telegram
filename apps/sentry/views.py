import hmac
import json
from _sha256 import sha256

from django.conf import settings

from rest_framework.generics import GenericAPIView

from .permissions import IsSentry


class WebhookAPIView(GenericAPIView):
    permission_classes = (IsSentry,)

    def post(self, request):
        pass
