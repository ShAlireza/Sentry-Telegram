import hmac
import json
from _sha256 import sha256

from django.conf import settings

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .permissions import IsSentry
from .models import Data


class WebhookAPIView(GenericAPIView):
    permission_classes = (IsSentry,)

    def post(self, request):
        data = request.data
        Data.objects.create(data=data, json=data)

        return Response(status=status.HTTP_200_OK)
