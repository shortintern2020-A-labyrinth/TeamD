from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import json
from default.models import get_video_category


@api_view(['GET'])
def category_view(request):
    # [{'id':18, 'name':'ショートムービー'}, ・・・]
    categories = get_video_category()
    return Response(
        categories,
        status=status.HTTP_200_OK
    )
